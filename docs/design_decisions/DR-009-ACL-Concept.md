```{dec_rec} One Format for Access Control List(s) (ACL)
   :id: dec_rec__platform__acl_concept
   :status: proposed
   :decision: open
```

   Context
   -------
   Access Control is required on multiple components; i.e.:
   
   - IPC (LoLa)
   Who is allowed to publish which services (who can create/modify a file in the according directory)
   For Service Providers: Once the IPC Channel/SharedMemory is created, whom to grant which rights to what area (data/control)
   This permissions will be based on uid.
   
   - SOME/IPC
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
   To prevent each component from implementing compeletley own mechanism for persmission enforcement; the decision schould be an alignment on a common ACL format, so that all components can use:
   - the same parser as a baselib to read the ACL
   - (optionally) the same "ACLHandler" to update/edit and recompile the ACL
   One additional big advantage of a harmonized ACL is that:
   - it is easier to review (security reviews, etc.)
   - it is easier to debug 
   - only one parser needs to be tested in depth
   - updates due to parser vulnerabilities can be centrallized
   
   The base proposal is as follows:
   - a json file as configuration
   - for runtime efficiency: compilation of the json file to a flatbuffer/binary file
   
   Proposed json format & properties (example): 
   
  
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
		  "criticality": "ASIL-B",
		  "version": 5,
		  "tlsenable": 1,
		  "ipsecenable": 1,
		  "macsecenable":1,			  
		  "specifics": {},
		  "allow": 
		  {
			"uids": 
			{
			  "101":{"rights": ["write"],"name": "oem.app.1","version": [],"criticality": "ASIL-B","specifics": {}},
			  "102":{"rights": ["read"],"name": "oem.app.2","version": [],"criticality": "ASIL-B","specifics": {}},
			  "103":{"rights": ["read"],"name": "tier1.daemon.1","version": [],"criticality": "ASIL-B","specifics": {}}
			},
			"ips": 
			{ 
				"10.1.15.2":{"name": "ecu_1","rights": ["write"],"version": [],"criticality": "QM","specifics": {}},
				"10.1.15.3":{"name": "ecu_2_app3","rights": ["read"],"version": [],"criticality": "QM","specifics": {}}
			}
		  }
		}
	  }
	}
  },
  "crypto": 
  {
	"0":
	{
		"keyspaceName": "tls_auth",
		"keys": 
		{
			"1":
			{	
				"name": "tls_auth_priv",
				"read": [],
				"use": [{"uid": 1,"otherid": "special_handling_1"},{"vmid": 4,"uid": 2}],
				"write": [{"uid": 1, "policy": "someipd_t"}]
			},
			"2":
			{ 
				"name": "tls_auth_pub",
				"read": [{"uid": -1}],
				"use": [{"uid": 1, "policy": ""},{"vmid": 4,"uid": 2}],
				"write": [{"uid": 1, "policy": "someipd_t"}]
			}
		}
	}
  }
}
```

	proposed json scheme:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/acl-policy.schema.json",
  "title": "ACL Configuration Schema",
  "type": "object",
  "additionalProperties": false,
  "required": [
	"policyVersion",
	"policyId",
	"defaultEffect",
	"generatedBy",
	"generatedAt",
	"services"
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
	  "propertyNames": {
		"$ref": "#/$defs/uint16Key"
	  },
	  "additionalProperties": {
		"$ref": "#/$defs/keyspace"
	  }
	}
  },
  "$defs": {
	"uint16Key": {
	  "type": "string",
	  "pattern": "^(0|[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
	},
	"uidKey": {
	  "type": "string",
	  "pattern": "^(0|[1-9][0-9]{0,8}|1[0-9]{9}|20[0-9]{8}|21[0-3][0-9]{7}|214[0-6][0-9]{6}|2147[0-3][0-9]{5}|21474[0-7][0-9]{4}|214748[0-2][0-9]{3}|2147483[0-5][0-9]{2}|21474836[0-3][0-9]|214748364[0-7])$"
	},
	"criticality": {
	  "type": "string",
	  "enum": [
		"QM",
		"ASIL-A",
		"ASIL-B",
		"ASIL-C",
		"ASIL-D"
	  ],
	  "maxLength": 128
	},
	"binaryFlag": {
	  "type": "integer",
	  "enum": [
		0,
		1
	  ]
	},
	"rights": {
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
		"criticality",
		"version",
		"tlsenable",
		"ipsecenable",
		"macsecenable",
		"specifics",
		"allow"
	  ],
	  "properties": {
		"providerName": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"criticality": {
		  "$ref": "#/$defs/criticality"
		},
		"version": {
		  "type": "integer",
		  "minimum": 0,
		  "maximum": 65535
		},
		"tlsenable": {
		  "$ref": "#/$defs/binaryFlag"
		},
		"ipsecenable": {
		  "$ref": "#/$defs/binaryFlag"
		},
		"macsecenable": {
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
		"version",
		"criticality",
		"specifics"
	  ],
	  "properties": {
		"name": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"rights": {
		  "$ref": "#/$defs/rights"
		},
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
		"criticality": {
		  "$ref": "#/$defs/criticality"
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
		"criticality",
		"specifics"
	  ],
	  "properties": {
		"name": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"rights": {
		  "$ref": "#/$defs/rights"
		},
		"criticality": {
		  "$ref": "#/$defs/criticality"
		},
		"specifics": {
		  "$ref": "#/$defs/specifics"
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
	"keyspace": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"keyspaceName",
		"keys"
	  ],
	  "properties": {
		"keyspaceName": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"keys": {
		  "type": "object",
		  "propertyNames": {
			"$ref": "#/$defs/uint16Key"
		  },
		  "additionalProperties": {
			"$ref": "#/$defs/key"
		  }
		}
	  }
	},
	"key": {
	  "type": "object",
	  "additionalProperties": false,
	  "required": [
		"name",
		"read",
		"use",
		"write"
	  ],
	  "properties": {
		"name": {
		  "type": "string",
		  "minLength": 1,
		  "maxLength": 128
		},
		"read": {
		  "$ref": "#/$defs/keyAccessList"
		},
		"use": {
		  "$ref": "#/$defs/keyAccessList"
		},
		"write": {
		  "$ref": "#/$defs/keyAccessList"
		}
	  }
	},
	"keyAccessList": {
	  "type": "array",
	  "items": {
		"$ref": "#/$defs/keyAccessEntry"
	  }
	},    
	"keyAccessEntry": {
	  "type": "object",
	  "additionalProperties": false,

	  "anyOf": [
		{
		  "required": ["uid"]
		},
		{
		  "required": ["policy"]
		},
		{
		  "required": ["vmid", "uid"]
		},
		{
		  "required": ["otherid"]
		}
	  ],

	  "dependentRequired": {
		"vmid": ["uid"]
	  },

	  "properties": {
		"vmid": {
		  "description": "Optional virtual machine ID. If present, uid is required as well.",
		  "type": "integer",
		  "minimum": 0,
		  "maximum": 2147483647
		},
		"uid": {
		  "type": "integer",
		  "minimum": -1,
		  "maximum": 2147483647
		},
		"policy": {
		  "type": "string",
		  "maxLength": 128
		},
		"otherid": {
		  "description": "Optional additional identifier for project-specific or non-UID based access control.",
		  "type": "string",
		  "maxLength": 128
		}
	  }
	}

  }
}
```
   

   Justification for the Decision
   ------------------------------
   open