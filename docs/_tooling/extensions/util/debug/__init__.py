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
import debugpy

port = 5678
if port is not None:
    debugpy.listen(('0.0.0.0', port))
    print('Waiting for client to connect on port: ' + str(port))
    debugpy.wait_for_client()



