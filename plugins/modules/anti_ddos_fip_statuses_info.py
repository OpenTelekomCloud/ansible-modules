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
module: anti_ddos_fip_statuses_info
short_description: Get Anti-DDoS statuses info
extends_documentation_fragment: opentelekomcloud.cloud.otc
version_added: "0.2.1"
author: "Irina Pereiaslavskaia (@irina-pereiaslavskaia)"
description:
  - Get Anti-DDoS defense statuses of all EIPs from the OTC.
  - EIP can been bound to an Elastic Cloud Server (ECS) or not.
options:
  ip:
    description: IP address, both IPv4 and IPv6 addresses are supported.
    type: str
  status:
    description: Defense status of ECS.
    choices: [normal, configging, notConfig, packetcleaning, packetdropping]
    type: str
requirements: ["openstacksdk", "otcextensions"]
'''

RETURN = '''
anti_ddos_fip_statuses_info:
  description: List of defense statuses of all EIPs from the OTC
  type: complex
  returned: On Success
  contains:
    floating_ip_address:
      description: Floating IP address.
      type: str
      sample: "192.168.42.221"
    floating_ip_id:
      description: ID of an EIP.
      type: str
      sample: "1867f954-fc11-4202-8247-6af2144867ea"
    network_type:
      description: EIP type. The value can be EIP or ELB.
      type: str
      sample: "EIP"
    status:
      description: Defense status.
      type: str
      sample: "notConfig"
'''

EXAMPLES = '''
# Get list of floating IPs statuses (all parameters are specified)
- opentelekomcloud.cloud.anti_ddos_fip_statuses_info:
    ip: "80.158.53.138"
    status: "normal"
  register: anti_ddos_fip_statuses

# Get list of floating IPs statuses (parameters are not specified)
- opentelekomcloud.cloud.anti_ddos_fip_statuses_info:
  register: anti_ddos_fip_statuses
'''

from ansible_collections.opentelekomcloud.cloud.plugins.module_utils.otc import OTCModule


class AntiDDoSFIPStatusesInfoModule(OTCModule):
    argument_spec = dict(
        ip=dict(type='str', required=False),
        status=dict(type='str',
                    choices=['normal', 'configging', 'notConfig',
                             'packetcleaning', 'packetdropping'],
                    required=False)
    )

    def run(self):

        ip_filter = self.params['ip']
        status_filter = self.params['status']

        data = []
        query = {}

        if ip_filter:
            query['ip'] = ip_filter

        if status_filter:
            query['status'] = status_filter

        for raw in self.conn.anti_ddos.floating_ips(**query):
            dt = raw.to_dict()
            dt.pop('location')
            data.append(dt)

        self.exit(changed=False, anti_ddos_statuses=data)


def main():
    module = AntiDDoSFIPStatusesInfoModule()
    module()


if __name__ == '__main__':
    main()
