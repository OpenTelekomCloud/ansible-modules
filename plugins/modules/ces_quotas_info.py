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
module: ces_quotas_info
short_description: Get ressource Quotas
extends_documentation_fragment: opentelekomcloud.cloud.otc
version_added: "0.3.0"
author: "Sebastian Gode (@SebastianGode)"
description:
  - Get ressource Quotas
requirements: ["openstacksdk", "otcextensions"]
'''

RETURN = '''
quotas:
    description: Dictionary of Quotas
    returned: changed
    type: list
    sample: [
        {
            "id": null,
            "name": null,
            "resources": [
                {
                    "id": null,
                    "location": null,
                    "name": null,
                    "quota": 100,
                    "type": "alarm",
                    "unit": "",
                    "used": 1
                }
            ]
        }
    ]
'''

EXAMPLES = '''
# Query Alarm Quotas
- opentelekomcloud.cloud.ces_quotas_info:
'''

from ansible_collections.opentelekomcloud.cloud.plugins.module_utils.otc import OTCModule


class CesQuotasInfoModule(OTCModule):
    argument_spec = dict()
    module_kwargs = dict(
        supports_check_mode=True
    )

    def run(self):

        data = []
        query = {}

        for raw in self.conn.ces.quotas(**query):
            dt = raw.to_dict()
            dt.pop('location')
            data.append(dt)

        self.exit(
            changed=False,
            quotas=data
        )


def main():
    module = CesQuotasInfoModule()
    module()


if __name__ == '__main__':
    main()
