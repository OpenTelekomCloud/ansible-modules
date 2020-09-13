#!/usr/bin/python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

DOCUMENTATION = '''
---
module: tasks
short_description: Get information about vpc peerings 
extends_documentation_fragment: opentelekomcloud.cloud.otc
version_added: "0.0.3"
author: "Polina Gubina (@polina-gubina)"
description:
  - Get a generator of vpc peerings info from the OTC.
options:
  name:
    description: Peering connection name.
    type: str
  status:
    description: Peering connection status.
    type: str
    choices: [PENDING_ACCEPTANCE, REJECTED, EXPIRED, DELETED, ACTIVE]
  tenant_id:
    description: Tenant ID.
    type: str
  vpc_id:
    description: VPC ID.
    type: str    
requirements: ["openstacksdk", "otcextensions"]
'''

RETURN = '''
peerings:
  description: The VPC peering connection object list.
  type: complex
  returned: On Success.
  contains:
    id:
      description: The VPC peering connection ID.
      type: str
      sample: "4dae5bac-0925-4d5b-add8-cb6667b8"
    name:
      description: The VPC peering connection name.
      type: str
      sample: "vpc-peering1"
    status:
      description: The VPC peering connection status.
      type: str
      sample: "ACTIVE"
    request_vpc_info:
      description: 	Information about the local VPC.
      type: complex
      sample: "{
                "tenant_id": "76889f64a23945ab887012be95acf",
                "vpc_id": "4dae5bac-0925-4d5b-add8-cb6667b8"
                }"
    accept_vpc_info:
      description:  Information about the peer VPC. 
      type: complex
      sample: "{
                "tenant_id": "968u64a23945ab887012be95acf",
                "vpc_id": "7dau5bac-0925-4d5b-add8-cb6667b8"
                }"
    description:
      description: Provides supplementary information about the VPC peering connection.
      type: str
      sample: ""
    created_at:
      description: The time (UTC) when the VPC peering connection is created.
      type: str
      sample: "2020-09-13T20:37:01"
    updated_at:
      description: Specifies the time (UTC) when the VPC peering connection is updated.
      type: str
      sample: "2020-09-13T20:38:02"
'''

EXAMPLES = '''
# Get configs versions.
- tasks:
    name: vpc_peering1
  register: vpc_peering
'''

from ansible_collections.opentelekomcloud.cloud.plugins.module_utils.otc import OTCModule


class VPCPeeringInfoModule(OTCModule):
    argument_spec = dict(
        name=dict(required=False),
        status=dict(required=False),
        tenant_id=dict(required=False),
        vpc_id=dict(required=False),
    )

    def run(self):

        name_filter = self.params['name']
        status_filter = self.params['status']
        tenant_id_filter = self.params['tenant_id']
        vpc_id_filter = self.params['vpc_id']

        data = []
        query = {}
        if name_filter:
            query['name'] = name_filter
        if status_filter:
            query['status'] = status_filter
        if tenant_id_filter:
            query['tenant_id'] = tenant_id_filter
        if vpc_id_filter:
            query['vpc_id'] = vpc_id_filter

        for raw in self.conn.vpc.peerings(**query):
            dt = raw.to_dict()
            dt.pop('location')
            data.append(dt)

        self.exit_json(
            changed=False,
            vpc_peerings=data
        )


def main():
    module = VPCPeeringInfoModule()
    module()


if __name__ == '__main__':
    main()