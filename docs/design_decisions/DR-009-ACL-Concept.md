.. dec_rec:: One Format for Access Control List(s) (ACL)
   :id: dec_rec__platform__acl_concept
   :status: proposed
   :version: 1
   :affects: <link>

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
   
   Proposed json format & properties: 
   
   {
  "policyVersion": 1,
  "policyId": "example-acl-policy-001",
  "defaultEffect": "deny",
  "generatedBy": "install-update-manager",
  "generatedAt": "2026-06-17T14:28:00Z",

  "services": 
  {
    111: //serviceID
	{
      "serviceName": "someservice",
      "serviceInstances": {
        500: //serviceInstanceID
		{
          "providerName": "fancy_name",
          "criticality": "ASIL-B",
          "version": 5,
		  "tlsenable": 1,
		  "ipsecenable": 1,
		  "macsecenable ":1,
		  //specifics is for oem/user specifics: e.g. some state machine aka allow access to everyone if in state X
          "specifics": {},
          "allow": 
		  {
            "uids": 
			{
			  //rights: "write" --> r+w to data & control, e.g. publisher in publish subscribe, m:n --> "m", 1:1 --> both
			  //        "read" --> r to data & rw on control, e.g. subscriber in publish subscribe, m:n --> "n"
			  //        "monitor" --> r to data & control, e.g. some health monitor checking duration of control blockers
			  //specifics is for oem/user specifics: e.g. allow uid 101 only to write/publish if in state X
              101:{"rights": ["write"],"name": "oem.app.1","version": [],"criticality": "ASIL-B","specifics": {}},
              102:{"rights": ["read"],"name": "oem.app.2","version": [],"criticality": "ASIL-B","specifics": {}},
              103:{"rights": ["read"],"name": "tier1.daemon.1","version": [],"criticality": "ASIL-B","specifics": {}}
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
  }
}
  
  "crypto": 
  {
	//keyspaceID
	0:
	{
		"keyspaceName": "tls_auth",
		"keys": 
		[
			//keyID
			1:
			{	
				"name": "tls_auth_priv",
				"read": [],
				"use": [{"uid": 1, "policy": ""},{"uid": 2, "policy": ""}],
				"write": [{"uid": 1, "policy": "someipd_t"}]
			},
			2:
			{ 
				"name": "tls_auth_pub",
				"read": [{"uid": -1, "policy": ""}],
				"use": [{"uid": 1, "policy": ""},{"uid": 2, "policy": ""}],
				"write": [{"uid": 1, "policy": "someipd_t"}]
			}
		]
    }
  }
}


   

   Justification for the Decision
   ------------------------------
   open