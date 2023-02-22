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
module: vpc_peering
short_description: Add/Update/Delete vpc peering connection from OpenTelekomCloud
extends_documentation_fragment: opentelekomcloud.cloud.otc
version_added: "0.13.1"
author: "Polina Gubina (@polina-gubina)"
description:
  - Add or Remove vpc peering from the OTC.
options:
  name:
    description:
        - Name or ID of the vpc peering connection.
        - Mandatory for creating.
        - Can be updated.
    type: str
    required: true
  description:
    description:
        - Provides supplementary information about the VPC peering connection.
    type: str
  local_router:
    description:
        - Name or ID of the local router.
        - Can not be updated.
    type: str
  local_project:
    description:
        - Specifies the ID of the project to which a local VPC belongs.
        - Can not be updated.
    type:  str
  remote_router:
    description:
        - ID of the remote router.
        - Can not be updated.
    type: str
  remote_project:
    description:
        - Specifies the ID of the project to which a peer VPC belongs.
        - Can not be updated.
    type: str
  state:
    description: Should the resource be present or absent.
    choices: [present, absent]
    default: present
    type: str
requirements: ["openstacksdk", "otcextensions"]
'''

RETURN = '''
vpc_peering:
  description: Dictionary describing VPC peering instance.
  type: complex
  returned: On Success.
  contains:
    id:
      description: Specifies the VPC peering connection ID.
      returned: On success when C(state=present)
      type: str
      sample: "39007a7e-ee4f-4d13-8283-b4da2e037c69"
    name:
      description: Specifies the VPC peering connection name.
      returned: On success when C(state=present)
      type: str
      sample: "vpc_peering1"
    status:
      description: Specifies the VPC peering connection status.
      returned: On success when C(state=present)
      type: str
      sample: "accepted"
    request_vpc_info:
      description: Dictionary describing the local vpc.
      returned: On success when C(state=present)
      type: complex
      contains:
        vpc_id:
          description: Specifies the ID of a VPC involved in a VPC peering connection.
          type: str
          sample: "39007a7e-ee4f-4d13-8283-b4da2e037c69"
        project_id:
          description: Specifies the ID of the project to which a VPC involved in the VPC peering connection belongs.
          type: str
          sample: "45007a7e-ee4f-4d13-8283-b4da2e037c69"
    accept_vpc_info:
      description: Dictionary describing the local vpc.
      returned: On success when C(state=present)
      type: complex
      contains:
        vpc_id:
          description: Specifies the ID of a VPC involved in a VPC peering connection.
          type: str
          sample: "39007a7e-ee4f-4d13-8283-b4da2e037c69"
        project_id:
          description: Specifies the ID of the project to which a VPC involved in the VPC peering connection belongs.
          type: str
          sample: "39007a7e-ee4f-4d13-8283-b4da2e037c69"
    description:
      description: Provides supplementary information about the VPC peering connection.
      returned: On success when C(state=present)
      type: str
      sample: ""
    created_at:
      description: Specifies the time (UTC) when the VPC peering connection is created.
      returned: On success when C(state=present)
      type: str
      sample: "2020-09-13T20:38:02"
    updated_at:
      description: Specifies the time (UTC) when the VPC peering connection is updated.
      returned: On success when C(state=present)
      type: str
      sample: "2020-09-13T20:38:02"
'''

EXAMPLES = '''
# Create a vpc peering.
- opentelekomcloud.cloud.vpc_peering:
    name: "peering1"
    local_router: "local-router"
    local_project: "959db9b6017d4a1fa1c6fd17b6820f55"
    remote_router: "peer-router"
    remote_project: "959db9b6017d4a1fa1c6fd17b6820f55"

# Update vpc perring
- opentelekomcloud.cloud.vpc_peering:
    name: "peering1"
    description: "new description"
    local_router: "local-router"
    local_project: "959db9b6017d4a1fa1c6fd17b6820f55"
    remote_router: "peer-router"
    remote_project: "959db9b6017d4a1fa1c6fd17b6820f55"

# Delete a load balancer(and all its related resources)
- opentelekomcloud.cloud.vpc_peering:
    name: "peering2"
    state: absent
'''

from ansible_collections.opentelekomcloud.cloud.plugins.module_utils.otc import OTCModule


class VPCPeeringModule(OTCModule):
    argument_spec = dict(
        name=dict(type='str', required=True),
        description=dict(type='str'),
        state=dict(default='present', choices=['absent', 'present']),
        local_router=dict(type='str'),
        local_project=dict(type='str'),
        remote_router=dict(type='str'),
        remote_project=dict(type='str')
    )
    module_kwargs = dict(
        required_if=[
            ('state', 'present', ['name', 'local_router', 'local_project',
                                  'remote_router', 'remote_project']),
        ],
        supports_check_mode=True
    )

    def _is_peering_exist(self, local_router_id, peer_router_id):
        for peering in self.conn.vpc.peerings():
            if (
                (
                    peering.local_vpc_info['vpc_id'] == local_router_id
                    and peering.peer_vpc_info['vpc_id'] == peer_router_id)
                or (
                    peering.local_vpc_info['vpc_id'] == peer_router_id
                    and peering.peer_vpc_info['vpc_id'] == local_router_id)
            ):
                return True
        return False

    def _is_same_peering(self, vpc_peering, local_router_id, peer_router_id):
        if vpc_peering.local_vpc_info['vpc_id'] == local_router_id\
                and vpc_peering.peer_vpc_info['vpc_id'] == peer_router_id:
            return True
        return False

    def _require_update(self, vpc_peering):
        if self.params['description']:
            if self.params['description'] != vpc_peering.description:
                return True
        return False

    def run(self):
        name = self.params['name']
        local_router = self.params['local_router']
        local_project = self.params['local_project']
        remote_router = self.params['remote_router']
        remote_project = self.params['remote_project']

        changed = False
        vpc_peering = self.conn.vpc.find_peering(name, ignore_missing=True)
        attrs = {}

        if self.params['state'] == 'present':
            local_router = self.conn.vpc.find_vpc(local_router,
                                                  ignore_missing=True)
            if not local_router:
                self.fail_json(msg="local router not found")
            remote_router = self.conn.vpc.find_vpc(remote_router,
                                                   ignore_missing=True)
            if not remote_router:
                self.fail_json(msg="remote router not found")

            if vpc_peering:
                if self._is_same_peering(vpc_peering, local_router.id,
                                         remote_router.id):
                    if self.params['description']:
                        attrs['description'] = self.params['description']
                    if self._require_update(vpc_peering):
                        changed = True
                        if self.ansible.check_mode:
                            self.exit_json(changed=changed)
                        vpc_peering = self.conn.vpc.update_peering(vpc_peering,
                                                                   **attrs)
                        self.exit_json(
                            changed=changed,
                            vpc_peering=vpc_peering
                        )
                    self.exit_json(changed=False)
            attrs = {}
            attrs['name'] = name
            attrs['local_vpc_info'] = {'vpc_id': local_router.id}
            attrs['peer_vpc_info'] = {'vpc_id': remote_router.id}
            if (
                    self.conn.current_project_id == local_project
                    and local_project != remote_project
            ):
                # Seems to be an API bug that doesn't want to see tenant_id
                # if A and B are in same project
                attrs['local_vpc_info']['tenant_id'] = local_project
                attrs['peer_vpc_info']['tenant_id'] = remote_project

            if self._is_peering_exist(local_router.id, remote_router.id):
                if self.ansible.check_mode:
                    self.exit_json(changed=False)
                self.fail_json(
                    msg="A VPC peering connection already exists between"
                        " the two routers."
                )
            if self.ansible.check_mode:
                self.exit_json(changed=True)
            vpc_peering = self.conn.vpc.create_peering(**attrs)
            self.exit_json(
                changed=True,
                vpc_peering=vpc_peering
            )

        elif self.params['state'] == 'absent':
            if vpc_peering:
                if self.ansible.check_mode:
                    self.exit_json(changed=True)
                self.conn.vpc.delete_peering(vpc_peering)
                changed = True
                self.exit_json(
                    changed=changed,
                    result="Resource was deleted"
                )
            self.exit_json(changed=False)


def main():
    module = VPCPeeringModule()
    module()


if __name__ == '__main__':
    main()
