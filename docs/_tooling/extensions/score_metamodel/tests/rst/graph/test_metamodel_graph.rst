..
   # *******************************************************************************
   # Copyright (c) 2025 Contributors to the Eclipse Foundation
   #
   # See the NOTICE file(s) distributed with this work for additional
   # information regarding copyright ownership.
   #
   # This program and the accompanying materials are made available under the
   # terms of the Apache License Version 2.0 which is available at
   # https://www.apache.org/licenses/LICENSE-2.0
   #
   # SPDX-License-Identifier: Apache-2.0
   # *******************************************************************************
#CHECK: check_metamodel_graph

.. feat_req:: Parent requirement
   :id: feat_req__parent__abcd
   :safety: QM
   :status: valid

#EXPECT: feat_req__child__abce: parent need `feat_req__parent__abcd` does not fulfill condition `{'and': ['safety != QM', 'status == valid']}`.

.. feat_req:: Child requirement
   :id: feat_req__child__abce
   :safety: ASIL_B
   :status: valid
   :satisfies: feat_req__parent__abcd


.. feat_req:: Parent requirement 2
   :id: feat_req__parent2__abcd
   :safety: ASIL_B
   :status: valid

#EXPECT-NOT: feat_req__child2__abce: parent need `feat_req__parent2__abcd` does not fulfill condition

.. feat_req:: Child requirement 2
   :id: feat_req__child2__abce
   :safety: ASIL_B
   :status: valid
   :satisfies: feat_req__parent__abcd
