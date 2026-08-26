# DR-003-ARCH-ACL-Concept: Common Access Control format for all components

```{dec_rec} One Format for Access Control (and following the Access Control List (ACL))
   :id: dec_rec__platform__acl_concept
   :status: proposed
   :context: Common Access Control format for all components
   :decision: open
```

   Context
   -------
   Access Control is required on multiple components; i.e.:
   
   - IPC (LoLa)
   Who is allowed to publish which services (who can create/modify a file in the according directory)
   For Service Providers: Once the IPC Channel/SharedMemory is created, whom to grant which rights to what area (data/control)
   This permissions will be based on uid.
   
   - SOME/IP
   Same to IPC, except the permissions will be based on IP address / netmask. 
   In addition: Should TLS be enforced for a service? Should IP & MACsec be active as basis for a certain service? 
   
   - Crypto
   Needs to know who (which application - i.e. which uid (every application shall run as own user))
   -- created/owns a key
   -- is allowed to write/change a key
   -- is allowed to use a key for any operations (e.g. sign/verify/encrypt/decrypt/keyderive/etc.)
   -- is allowed to read/extract a key (e.g. pub keys)

   Consequences
   ------------
   To prevent each component from implementing completley own mechanism for permission enforcement; the decision should be an alignment on a common ACL format, so that all components can use:
   - the same parser as a baselib to read the ACL
   - (optionally) the same "ACLHandler" to update/edit and recompile the ACL
   One additional big advantage of a harmonized ACL is that:
   - it is easier to review (security reviews, etc.)
   - it is easier to debug 
   - only one parser needs to be tested in depth
   - updates due to parser vulnerabilities can be centralized
   
   The base proposal is as follows:
   - a json file as configuration
   - for runtime efficiency: compilation of the json file to a flatbuffer/binary file
  
   Proposed json format & properties (example at the bottom): 

   proposed json scheme:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "acl-policy.schema.json",
  "title": "ACL Configuration Schema",
  "type": "object",
  "additionalProperties": false,
  "required": [
	"policyVersion",
	"policyId",
	"defaultEffect",
	"generatedBy",
	"generatedAt"
  ],
  "properties": {
	"policyVersion": {
	  "type": "integer",
	  "minimum": 1
	},
	"policyId": {
	  "type": "string",
	  "minLength": 1,
	  "maxLength": 128
	},
	"defaultEffect": {
	  "description": "If an entry cannot be found this means it is either allowed or denied by default which can be set by this option. More finegrained deny/allow default operations overrule the generic one here (e.g. crypto/certs).",
	  "type": "string",
	  "enum": [
		"deny",
		"allow"
	  ],
	  "maxLength": 128
	},
	"generatedBy": {
	  "type": "string",
	  "minLength": 1,
	  "maxLength": 128
	},
	"generatedAt": {
	  "type": "string",
	  "description": "ISO-8601 UTC timestamp without fractional seconds",
	  "maxLength": 20,
	  "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
	},
	"services": {
	  "type": "object",
	  "propertyNames": {
		"$ref": "#/$defs/uint16Key"
	  },
	  "additionalProperties": {
		"$ref": "#/$defs/service"
	  }
	},
	"crypto": {
	  "type": "object",
	  "additionalProperties": false,	 
	  "properties": {
		"profiles": {
		  "description": "Profiles can be defined as references if multiple applications need the same rights, they can be just assigned a profile.",
		  "type": "object",
		  "propertyNames": {
			"type": "string",
			"minLength": 1,
			"maxLength": 128
		  },
		  "additionalProperties": {
			"$ref": "#/$defs/cryptoProfile"
		  }
		},
		"operationalRights": {
		  "description": "Operational rights are general rights who are independant of a specific key or certificate stored in the cryptostorage.",
		  "type": "object",
		  "propertyNames": {
			"description": "The default right defines the behavior if an identifier (uid, vmid|uid or otherid is not defined at all but wants to execute a functionality or access a certificate or key. This means in the highest securitysetting default right is empty, or only allows non key related operations like hashing only by default.)",
			"anyOf": [
			  {
				"const": "default"
			  },
			  {
				"$ref": "#/$defs/subjectKey"
			  }
			]
		  },
		  "additionalProperties": {
			"$ref": "#/$defs/operationalRight"
		  }
		},
		"keys": {
		  "type": "object",	  
		  "additionalProperties": {
			"$ref": "#/$defs/key"
		  }
		},
		"truststore": {
		  "$ref": "#/$defs/truststore"
		},
		"certs": { 
		  "$ref": "#/$defs/certs"
		}
	  }
	}
  },
  "$defs": {
    "version": {
	  "type": "array",
	  "items": {
	    "anyOf": [
		  {
			"type": "integer",
			"minimum": 0,
			"maximum": 65535
		  },
		  {
			"type": "string",
			"maxLength": 128
		  }
		]
	  }
	},
	"uint16Key": {
	  "type": "string",
	  "pattern": "^(0|[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
	},
	"uidKey": {
	  "type": "string",
	  "pattern": "^(0|[1-9][0-9]{0,8}|1[0-9]{9}|20[0-9]{8}|21[0-3][0-9]{7}|214[0-6][0-9]{6}|2147[0-3][0-9]{5}|21474[0-7][0-9]{4}|214748[0-2][0-9]{3}|2147483[0-5][0-9]{2}|21474836[0-3][0-9]|214748364[0-7])$"
	},
	"binaryFlag": {
	  "type": "integer",
	  "enum": [
		0,
		1
	  ]
	},
	"specifics": {
	  "description": "OEM-specific or project-specific extension object. Unknown properties are allowed only here.",
	  "type": "object",
	  "additionalProperties": {
		"$ref": "#/$defs/specificValue"
	  }
	},
	"specificValue": {
	  "anyOf": [
		{
		  "type": "string",
		  "maxLength": 128
		},
		{
		  "type": "number"
		},
		{
		  "type": "integer"
		},
		{
		  "type": "boolean"
		},
		{
		  "type": "null"
		},
		{
		  "type": "array",
		  "items": {
			"$ref": "#/$defs/specificValue"
		  }
		},
		{
		  "type": "object",
		  "additionalProperties": {
			"$ref": "#/$defs/specificValue"
		  }
		}
	  ]
	},
	"service": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"serviceName",
		"serviceInstances"
	  ],
	  "properties": {
		"serviceName": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"serviceInstances": {
		  "type": "object",
		  "propertyNames": {
			"$ref": "#/$defs/uint16Key"
		  },
		  "additionalProperties": {
			"$ref": "#/$defs/serviceInstance"
		  }
		}
	  }
	},
	"serviceInstance": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"providerName",
		"version",
		"precondition_tlsenabled",
		"precondition_ipsecenabled",
		"precondition_macsecenabled",
		"specifics",
		"allow"
	  ],
	  "properties": {
		"providerName": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"version": {
		  "type": "integer",
		  "minimum": 0,
		  "maximum": 65535
		},
		"precondition_tlsenabled": {
		  "$ref": "#/$defs/binaryFlag"
		},
		"precondition_ipsecenabled": {
		  "$ref": "#/$defs/binaryFlag"
		},
		"precondition_macsecenabled": {
		  "$ref": "#/$defs/binaryFlag"
		},
		"specifics": {
		  "$ref": "#/$defs/specifics"
		},
		"allow": {
		  "$ref": "#/$defs/allow"
		}
	  }
	},
	"allow": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"uids",
		"ips"
	  ],
	  "properties": {
		"uids": {
		  "type": "object",
		  "propertyNames": {
			"$ref": "#/$defs/uidKey"
		  },
		  "additionalProperties": {
			"$ref": "#/$defs/uidSubject"
		  }
		},
		"ips": {
		  "type": "object",
		  "propertyNames": {
			"$ref": "#/$defs/ipOrCidrKey"
		  },
		  "additionalProperties": {
			"$ref": "#/$defs/ipSubject"
		  }
		}
	  }
	},
	"uidSubject": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"name",
		"rights",
		"specifics"
	  ],
	  "properties": {
		"name": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"rights": {
		  "$ref": "com.rights.schema.json"
		},
		"version": {
		  "$ref": "#/$defs/version"
		},
		"specifics": {
		  "$ref": "#/$defs/specifics"
		}
	  }
	},
	"ipSubject": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"name",
		"rights",
		"specifics"
	  ],
	  "properties": {
		"name": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"rights": {
		  "$ref": "com.rights.schema.json"
		},
		"specifics": {
		  "$ref": "#/$defs/specifics"
		},
		"version": {
		  "$ref": "#/$defs/version"
		}
	  }
	},
	"ipOrCidrKey": {
	  "type": "string",
	  "maxLength": 128,
	  "anyOf": [
		{
		  "description": "IPv4 address",
		  "pattern": "^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
		},
		{
		  "description": "IPv4 CIDR subnet",
		  "pattern": "^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}\\/(3[0-2]|[1-2]?[0-9])$"
		},
		{
		  "description": "IPv6 address or IPv6 CIDR subnet, simplified validation",
		  "pattern": "^([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}(\\/(12[0-8]|1[0-1][0-9]|[1-9]?[0-9]))?$"
		}
	  ]
	},
	"key": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"read",
		"use",
		"modify"
	  ],
	  "properties": {
		"read": {
		  "$ref": "#/$defs/keyAccessMap"
		},
		"use": {
		  "$ref": "#/$defs/keyAccessMap"
		},
		"modify": {
		  "$ref": "#/$defs/keyAccessMap"
		}
	  }
	},
	"subjectKey": {
      "type": "string",
      "maxLength": 512,
      "description": "Canonical access subject key. Components use '=' and are separated by '|'. Fixed order: otherid, vmid, uid, policy. Components in one key have AND semantics.",
      "oneOf": [
        {
          "description": "UID only, optionally followed by policy",
          "pattern": "^uid=(-1|0|[1-9][0-9]{0,9})(\\|policy=[A-Za-z0-9._-]+)?$"
        },
        {
          "description": "VMID and UID, optionally followed by policy",
          "pattern": "^vmid=(0|[1-9][0-9]{0,9})\\|uid=(-1|0|[1-9][0-9]{0,9})(\\|policy=[A-Za-z0-9._-]+)?$"
        },
        {
          "description": "Other ID alone, or with UID, optionally followed by policy",
          "pattern": "^otherid=[A-Za-z0-9._-]+(\\|uid=(-1|0|[1-9][0-9]{0,9}))?(\\|policy=[A-Za-z0-9._-]+)?$"
        },
        {
          "description": "Other ID, VMID and UID, optionally followed by policy",
          "pattern": "^otherid=[A-Za-z0-9._-]+\\|vmid=(0|[1-9][0-9]{0,9})\\|uid=(-1|0|[1-9][0-9]{0,9})(\\|policy=[A-Za-z0-9._-]+)?$"
        },
        {
          "description": "Policy only",
          "pattern": "^policy=[A-Za-z0-9._-]+$"
        }
      ]
    },
    "cryptoOperation": {
	  "description" : "Right now this enum is listed in the ACL, in the future this will reference to the schema of the crypto configuration (not ACL) so that if functionality is added/removed it only needs to be changed on one place",
      "type": "string",
      "enum": [
        "hash",
        "encrypt",
        "decrypt",
        "sign",
        "verify",
        "keyderive",
        "wrap",
        "unwrap",
        "mac",
        "random",
        "keygen",
        "keyimport",
        "keyexport",
        "keydelete"
      ]
    },
    "keyAccessOptions": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "operations": {
          "description": "Optional restriction to the listed cryptographic operations. If absent, the access category itself is not further restricted by operation.",
          "type": "array",
          "minItems": 1,
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/cryptoOperation"
          }
        }
      }
    },
	"keyAccessMap": {
	  "type": "object",
	  "propertyNames": {
		"$ref": "#/$defs/subjectKey"
	  },
      "additionalProperties": {
        "$ref": "#/$defs/keyAccessOptions"
      }
	},
	"subjectList": {
	  "type": "array",
	  "uniqueItems": true,
	  "items": {
		"$ref": "#/$defs/subjectKey"
	  }
	},
	"truststoreEntry": {
	  "description" : "This will only define who can modify the content of a truststore, which certificates belong to the truststore is defined in the crypto config.",
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"modify",
		"confirmTrusted"
	  ],
	  "properties": {
		"modify": {  
		  "$ref": "#/$defs/subjectList"
		},
		"confirmTrusted": {
			"description": "If put to True, then even though an application A might have rights to modify/update a certificate in a certificate slot, the owner of the truststore must accept it, otherwhise it will be marked invalid for the truststore. If put to False, if application A has rights to modify/uipdate a certificate, then its by default trusted by the other parties as well.",
			"type": "boolean"
		}
	  }
	},
	"truststore": {
	  "type": "object",
	  "additionalProperties": {
		"$ref": "#/$defs/truststoreEntry"
	  }
	},
	"cert": {
	  "description": "The usual usecase is that certifcates are public, so it is expected that only modify is used - if at all. However if a certificate might have e.g. privacy related data, it also allows to restrict the read or use access.",
	  "type": "object",
	  "additionalProperties": false,
	  "required": [],
	  "properties": {
		"modify": {				
		  "$ref": "#/$defs/subjectList"	 
		},
		"read": {
		  "$ref": "#/$defs/keyAccessMap"
		},
		"use": {
		  "$ref": "#/$defs/keyAccessMap"
		}
	  }
	},
	"certs": {
	  "type": "object",
	  "properties": {
		"defaultReadDeny": {
		  "type": "boolean"
		},
		"defaultWriteDeny": {
		  "type": "boolean"
		}
	  },
	  "patternProperties": {
		"^(?!defaultReadDeny$|defaultWriteDeny$).+$": {	 
		  "$ref": "#/$defs/cert"
		}
	  },
	  "additionalProperties": false
	},    
	"memoryLimiting": {
	  "description": "To enhance resistance to DoS, it is possible to restrict the access to memory for applications. With that it means the total memory an application can use to store keys or certificates. This can be either defined in slots and/or in bytes.",
	  "type": "object",
	  "additionalProperties": false,
	  "minProperties": 1,
	  "properties": {
		"bytes": {
		  "type": "integer",
		  "minimum": 0
		},
		"slots": {
		  "type": "integer",
		  "minimum": 0
		}
	  }
	},
	"jobLimiting": {
	  "description": "Job limiting enhances resistances to DoS; it is possible to restrict the executions a application is allowed to do.",
	  "oneOf": [
		{
		  "description": "Parallel means that an application is allowed to execute a maximum of X Jobs in parallel.",
		  "type": "object",
		  "additionalProperties": false,
		  "required": ["parallel"],
		  "properties": {
			"parallel": {
			  "type": "integer",
			  "minimum": 1
			}
		  }
		},
		{
		  "description": "Interval limits the execution X jobs per interval. An interval can be an cycle (not further defined, to be customized in an application project), or in seconds.",
		  "type": "object",
		  "additionalProperties": false,
		  "required": ["interval", "intervaltype"],
		  "properties": {
			"interval": {
			  "type": "integer",
			  "minimum": 1
			},
			"intervaltype": {
			  "type": "string",
			  "enum": ["cycle", "second"]
			}
		  }
		}
	  ]
	},
	"cryptoProviderRights": {
	  "type": "object",
	  "additionalProperties": false,
	  "properties": {
		"operations": {
		  "description": "Operations not using a key from a configured keyspace, including operations where the caller supplies the key with the request.",
		  "type": "array",
		  "minItems": 1,
		  "uniqueItems": true,
		  "items": {
			"$ref": "#/$defs/cryptoOperation"
		  }
		},
		"memoryLimiting": {
		  "$ref": "#/$defs/memoryLimiting"
		},
		"jobLimiting": {
		  "$ref": "#/$defs/jobLimiting"
		}
	  }
	},
	"providerSpecific": {
	  "type": "object",
	  "minProperties": 1,
	  "propertyNames": {
		"type": "string",
		"minLength": 1,
		"maxLength": 48
	  },
	  "additionalProperties": {
		"$ref": "#/$defs/cryptoProviderRights"
	  }
	},
	"cryptoRights": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"providerspecific"
	  ],
	  "properties": {
		"providerspecific": {
		  "$ref": "#/$defs/providerSpecific"
		}
	  }
	},
	"cryptoProfile": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"rights"
	  ],
	  "properties": {		
		"rights": {
		  "$ref": "#/$defs/cryptoRights"
		}
	  }
	},
	"operationalRight": {
	  "type": "object",
	  "additionalProperties": false,
	  "properties": {
		"cryptoDaemonSharedMemMaxSizeDefault": {
		  "$ref": "#/$defs/memoryLimiting"
		},
		"cryptoDaemonSharedMemMaxSize": {
		  "$ref": "#/$defs/memoryLimiting"
		},
		"profileId": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"providerspecific": {
		  "$ref": "#/$defs/providerSpecific"
		}
	  },
	  "oneOf": [
		{
		  "required": ["profileId"]
		},
		{
		  "required": ["providerspecific"]
		}
	  ]
	}
  }
}
```
   Own rights schema which (can be if required adapted) for communication (IPC, SOME/IP)
   Default support for:
   read := subscribe/1:1/consume/request aka receive response
   write := publish/1:1/produce/send response
   monitor := observe, without ability to lock while reading or influence the program flow

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "com.rights.schema.json",
  "title": "Access Control for Communication Schema",
  "description": "Allowed access rights for communication.",
  "type": "array",
  "items": {
    "type": "string",
    "enum": [
      "read",
      "write",
      "monitor"
    ],
    "maxLength": 128
  },
  "uniqueItems": true
}

```

   Example:

```json
{
  "policyVersion": 1,
  "policyId": "example-acl-policy-001",
  "defaultEffect": "deny",
  "generatedBy": "install-update-manager",
  "generatedAt": "2026-06-17T14:28:00Z",

  "services": 
  {
	"111":
	{
	  "serviceName": "someservice",
	  "serviceInstances": {
		"500":
		{
		  "providerName": "fancy_name",		  
		  "version": 5,
		  "precondition_tlsenabled": 1,
		  "precondition_ipsecenabled": 1,
		  "precondition_macsecenabled":1,			  
		  "specifics": {},
		  "allow": 
		  {
			"uids": 
			{
			  "101":{"rights": ["write"],"name": "oem.app.1","version": [],"specifics": {}},
			  "102":{"rights": ["read"],"name": "oem.app.2","version": [],"specifics": {}},
			  "103":{"rights": ["read"],"name": "tier1.daemon.1","version": [],"specifics": {}}
			},
			"ips": 
			{ 
				"10.1.15.2":{"name": "ecu_1","rights": ["write"],"version": [],"specifics": {}},
				"10.1.15.3":{"name": "ecu_2_app3","rights": ["read"],"version": [],"specifics": {}}
			}
		  }
		}
	  }
	}
  },
  "crypto": 
  {
	"profiles":
	{
		"encrypt_and_sign_software":
		{
			"rights":
			{
				"providerspecific":
				{
					"Software":
					{
						"operations": ["hash","keygen","keyimport"],
						"memoryLimiting": {"slots":4,"bytes":896},
						"jobLimiting": {"parallel":3}				
					}
				}
			}
		},
		"hash":
		{
			"rights":
			{
				"providerspecific":
				{
					"Software":
					{
						"operations":["hash"],
						"memoryLimiting": {"slots":0},
						"jobLimiting":{"parallel":1}
					}
				}
			}
		}
	},
	"operationalRights": 
	{
		"default":
		{
			"cryptoDaemonSharedMemMaxSizeDefault":{"bytes":20000},
			"profileId": "hash"
		},		
		"uid=1": 
		{
			"cryptoDaemonSharedMemMaxSize":{"bytes":10000},
			"providerspecific":
			{
				"Software":
				{
					"operations": ["hash","keygen","keyimport"],
					"memoryLimiting": {"bytes":8178},
					"jobLimiting": {"parallel":3}				
				},
				"PKCS11_HW":
				{
					"operations": ["hash"],
					"memoryLimiting": {"slots":4,"bytes":896},
					"jobLimiting": {"parallel":1}	
				}
			}
		},
		"vmid=3|uid=1": 
		{
			"profileId":"encrypt_and_sign_software"
		},
		"otherid=someipd": 
		{
			"providerspecific":
			{
				"PKCS11_HW":
				{
					"operations": ["hash"],
					"memoryLimiting": {"slots":4},
					"jobLimiting": {"parallel":1}	
				}
			}
		}
	},

	"keys":
	{
		"hw_keyslot1":	
		{
			"read": {},
			"use":
			{
				"otherid=special_handling_1|uid=1": {},
				"vmid=4|uid=2": {"operations": ["sign"]}
			},
			"modify":
			{
				"uid=1|policy=someipd_t": {}
			}
		},
		"sw_keyslot1":
		{
			"read": 
			{
				"uid=-1":{}
			},
			"use": 
			{
				"uid=1": {},
				"vmid=4|uid=2": {}
			},
			"modify": 
			{
				"uid=1|policy=someipd_t":{}
			}
		}
	},
	"truststore":
	{
		"trusted_signees":
		{
			"confirmTrusted":false,
			"modify": ["vmid=4|uid=2"]
		}

	},

	"certs":
	{
		"defaultReadDeny":false,
		"defaultWriteDeny":true,
		"signing_root": 
		{
			"modify":[]					
		},
		"signing_authority_1":
		{
			"modify":["uid=1"]
		}
	}
}
}
```

   Justification for the Decision
   ------------------------------
   open