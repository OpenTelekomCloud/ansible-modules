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
module: lb_member_info
short_description: Get backend server group member info from OpenTelekomCloud
extends_documentation_fragment: opentelekomcloud.cloud.otc
version_added: "0.0.3"
author: "Anton Sidelnikov (@anton-sidelnikov)"
description:
  - Get Enhanced Load Balancer members from the OTC.
options:
  name:
    description:
      - Optional name or id of the member.
    type: str
  project_id:
    description:
      - Optional the ID of the project where the backend server is used.
    type: str
  address:
    description:
      - Optional the private IP address of the backend server.
    type: str
  protocol_port:
    description:
      - Optional the port used by the backend server.
    type: int
  subnet:
    description:
      - Optional the ID or Name of the subnet where the backend server works.
    type: str
  admin_state_up:
    description:
      - Optional the administrative status of the backend server.
    type: bool
  weight:
    description:
      - Optional the backend server weight.
    type: int
  pool:
    description:
      - Specifies the ID or Name of the backend server group.
    type: str
    required: true
requirements: ["openstacksdk", "otcextensions"]
'''

RETURN = '''
members:
  description: Dictionary describing members.
  type: complex
  returned: On Success.
  contains:
    id:
      description: Specifies the backend server ID.
      type: str
      sample: "39007a7e-ee4f-4d13-8283-b4da2e037c69"
    name:
      description: Specifies the backend server name.
      type: str
      sample: "bs_test"
    address:
      description: Specifies the private IP address of the backend server.
      type: str
    protocol_port:
      description: Specifies the port used by the backend server.
      type: int
    subnet_id:
      description: Specifies the ID of the subnet where the backend server works.
      type: str
    admin_state_up:
      description: Specifies the administrative status of the backend server.
      type: bool
    weight:
      description: Specifies the backend server weight.
      type: int
    operating_status:
      description: Specifies the health check result of the backend server.
      type: str
    members_links:
      description: Provides links to the previous or next page during pagination query, respectively.
      type: list
'''

EXAMPLES = '''
# Get a lb member info.
- lb_member_info:
    state: present
    name: member-test
  register: lb_mmbr_info
'''

from ansible_collections.opentelekomcloud.cloud.plugins.module_utils.otc import OTCModule


class LoadBalancerMemberInfoModule(OTCModule):
    argument_spec = dict(
        name=dict(required=False),
        pool=dict(required=True),
        project_id=dict(required=False, type='str'),
        address=dict(required=False, type='str'),
        protocol_port=dict(required=False, type='int'),
        subnet=dict(required=False, type='str'),
        admin_state_up=dict(required=False, type='bool'),
        weight=dict(required=False, type='int')
    )

    def run(self):
        name_filter = self.params['name']
        project_id_filter = self.params['project_id']
        address_filter = self.params['address']
        protocol_port_filter = self.params['protocol_port']
        subnet_filter = self.params['subnet']
        admin_state_filter = self.params['admin_state_up']
        weight_filter = self.params['weight']

        data = []
        args = {}

        if name_filter:
            args['name'] = name_filter
        if project_id_filter:
            args['tenant_id'] = project_id_filter
        if address_filter:
            args['address'] = address_filter
        if protocol_port_filter:
            args['protocol_port'] = protocol_port_filter
        if subnet_filter:
            subnet = self.conn.network.find_subnet(name_or_id=name_filter)
            if subnet:
                args['subnet_id'] = subnet.id
        if admin_state_filter:
            args['admin_state_up'] = admin_state_filter
        if weight_filter:
            args['weight'] = weight_filter

        pool = self.conn.network.find_pool(name_or_id=self.params['pool'])
        if self.params['name']:
            raw = self.conn.network.find_pool_member(pool=pool, name_or_id=name_filter)
            dt = raw.to_dict()
            dt.pop('location')
            data.append(dt)
        else:
            for raw in self.conn.network.pool_members(pool=pool, **args):
                dt = raw.to_dict()
                dt.pop('location')
                data.append(dt)

        self.exit_json(
            changed=False,
            members=data
        )


def main():
    module = LoadBalancerMemberInfoModule()
    module()


if __name__ == '__main__':
    main()
