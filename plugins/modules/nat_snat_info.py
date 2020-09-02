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
module: nat_snat_info
short_description: Get SNAT rule details
extends_documentation_fragment: opentelekomcloud.cloud.otc
version_added: "0.0.1"
author: "Sebastian Gode (@SebastianGode)"
description:
  - Get a SNAT Rule Details.
requirements: ["openstacksdk", "otcextensions"]
options:
  admin_state_up:
    description:
      - NAT rule state.
    type: str
  cidr:
    description:
      - Specifies a subset of the VPC subnet Classless Inter-Domain Routing block or a CIDR block of Direct Connect
    type: str
  created_at:
    description:
      - Creation time of the rule
    type: str
  floating_ip_address:
    description:
      - Assigned floating IP
    type: str
  floating_ip_id:
    description:
      - ID of the floating IP
    type: str
  id:
    description:
      - ID the rule
    type: str
  nat_gateway_id:
    description:
      - ID of the NAT gateway
    type: str
  network_id:
    description:
      - ID of the assigned network
    type: str
  project_id:
    description:
      - Filters SNAT rules for the project ID
    type: str
  source_type:
    description:
      - 0 Either network id or cidr can be specified in VPC ... 1 only cidr can be specified over Direct Connect
    type: str
  status:
    description:
      - rule enabled or disable
    type: str

'''

RETURN = '''
---
snat_list:
    description: List of SNAT rules.
    type: complex
    returned: On Success.
    contains:
        admin_state_up:
            description: NAT rule state
            type: str
            sample: "True"
        cidr:
            description: Specifies a subset of the VPC subnet Classless Inter-Domain Routing block or a CIDR block of Direct Connect
            type: str
            sample: "null"
        created_at:
            description: Creation time
            type: str
            sample: "yyyy-mm-dd hh:mm:ss"
        floating_ip_address:
            description: Assigned Floating IP Address
            type: str
            sample: "123.1.2.3"
        floating_ip_id:
            description: Assigned Floating IP ID
            type: str
            sample: "39007a7e-ee4f-4d13-8283-b4da2e037c69"
        id:
            description: ID of the SNAT rule
            type: str
            sample: "25d24fc8-d019-4a34-9fff-0a09fde6a123"
        nat_gateway_id:
            description: NAT Gateway ID
            type: str
            sample: "25d24fc8-d019-4a34-9fff-0a09fde6a123"
        network_id:
            description: ID of the attached Network
            type: str
            sample: "25d24fc8-d019-4a34-9fff-0a09fde6a123"
        project_id:
            description: ID of the Project where the SNAT rule is located in
            type: str
            sample: "16d53a84a13b49529d2e2c3646612345"
        source_type:
            description: 0 Either network id or cidr can be specified in VPC ... 1 only cidr can be specified over Direct Connect
            type: str
            sample: "0"
        status:
            description: NAT rule status
            type: str
            sample: "ACTIVE"

'''

EXAMPLES = '''
# Get configs versions.
- nat_snat_info:
  register: sn

- nat_snat_info:
    status: "ACTIVE"
  register: sn

- nat_snat_info:
    status: "ACTIVE"
    source_type: "0"
  register: sn
'''

from ansible_collections.opentelekomcloud.cloud.plugins.module_utils.otc import OTCModule


class NATGatewayInfoModule(OTCModule):
    argument_spec = dict(
        admin_state_up=dict(required=False),
        cidr=dict(required=False),
        created_at=dict(required=False),
        floating_ip_address=dict(required=False),
        floating_ip_id=dict(required=False),
        id=dict(required=False),
        nat_gateway_id=dict(required=False),
        network_id=dict(required=False),
        source_type=dict(required=False),
        status=dict(required=False),
        project_id=dict(required=False)
    )

    def run(self):
        admin_state_up_filter = self.params['admin_state_up']
        cidr_filter = self.params['cidr']
        created_at_filter = self.params['created_at']
        floating_ip_address_filter = self.params['floating_ip_address']
        floating_ip_id_filter = self.params['floating_ip_id']
        id_filter = self.params['id']
        nat_gateway_id_filter = self.params['nat_gateway_id']
        network_id_filter = self.params['network_id']
        source_type_filter = self.params['source_type']
        status_filter = self.params['status']
        project_id_filter = self.params['project_id']

        data = []

        for raw in self.conn.nat.snat_rules():
            if (admin_state_up_filter is None):
                pass
            elif ((admin_state_up_filter and not raw.admin_state_up) or
                    (not admin_state_up_filter and raw.admin_state_up)):
                continue
            if (cidr_filter and raw.cidr != cidr_filter):
                continue
            if (created_at_filter and raw.created_at != created_at_filter):
                continue
            if (floating_ip_address_filter and raw.floating_ip_address
                    != floating_ip_address_filter):
                continue
            if (floating_ip_id_filter and raw.floating_ip_id
                    != floating_ip_id_filter):
                continue
            if (id_filter and raw.id != id_filter):
                continue
            if (nat_gateway_id_filter and raw.nat_gateway_id
                    != nat_gateway_id_filter):
                continue
            if (network_id_filter and raw.network_id != network_id_filter):
                continue
            if (source_type_filter and raw.source_type != source_type_filter):
                continue
            if (status_filter and raw.status != status_filter):
                continue
            if (project_id_filter and raw.project_id != project_id_filter):
                continue
            dt = raw.to_dict()
            dt.pop('location')
            data.append(dt)

        self.exit(
            changed=False,
            snat_list=data
        )


def main():
    module = NATGatewayInfoModule()
    module()


if __name__ == '__main__':
    main()
