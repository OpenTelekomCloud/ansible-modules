.. _opentelekomcloud.cloud.nat_dnat_rule_module:


************************************
opentelekomcloud.cloud.nat_dnat_rule
************************************

**Manage NAT DNAT rules**


Version added: 0.0.6

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manage NAT DNAT rules



Requirements
------------
The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36.0
- otcextensions
- python >= 3.6


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>admin_state_up</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>DNAT rule state.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>api_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Dictionary containing auth information as needed by the cloud&#x27;s auth plugin strategy. For the default <em>password</em> plugin, this would contain <em>auth_url</em>, <em>username</em>, <em>password</em>, <em>project_name</em> and any information about domains (for example, <em>os_user_domain_name</em> or <em>os_project_domain_name</em>) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auth_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the <em>auth</em> parameter should be updated accordingly.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ca_cert</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A path to a CA Cert bundle that can be used as part of verifying SSL API requests.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: cacert</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_cert</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A path to a client certificate to use as part of the SSL transaction.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: cert</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A path to a client key to use as part of the SSL transaction.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: key</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cloud</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Named cloud or cloud config to operate against. If <em>cloud</em> is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for <em>auth</em> and <em>auth_type</em>. This parameter is not needed if <em>auth</em> is provided or if OpenStack OS_* environment variables are present. If <em>cloud</em> is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>external_service_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the port for providing external services.</div>
                        <div>Mandatory for DNAT rule creation</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>floating_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ID or Name of the floating IP</div>
                        <div>Mandatory for DNAT rule creation</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ID of the DNAT rule</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>admin</li>
                                    <li>internal</li>
                                    <li><div style="color: blue"><b>public</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Endpoint URL type to fetch from the service catalog.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: endpoint_type</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>internal_service_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the port used by ECSs or BMSs to provide services for external systems</div>
                        <div>Mandatory for DNAT rule creation</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nat_gateway</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ID or Name of the NAT gateway</div>
                        <div>Mandatory for DNAT rule creation</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the port ID of an ECS or a BMS. This parameter and private_ip are alternative</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the private IP address, for example, the IP address of a Direct Connect connection. This parameter and port are alternative</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>project_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the project ID</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>tcp</b>&nbsp;&larr;</div></li>
                                    <li>udp</li>
                                    <li>any</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the protocol type. Currently, TCP, UDP, and ANY are supported.</div>
                        <div>Mandatory for DNAT rule creation</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>region_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the region.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>Instance state</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">180</div>
                </td>
                <td>
                        <div>How long should ansible wait for the requested resource.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Whether or not SSL API requests should be verified.</div>
                        <div>Before Ansible 2.3 this defaulted to <code>yes</code>.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: verify</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wait</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Should ansible wait until the requested resource is complete.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - The standard OpenStack environment variables, such as ``OS_USERNAME`` may be used instead of providing explicit values.
   - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at https://docs.openstack.org/openstacksdk/



Examples
--------

.. code-block:: yaml+jinja

    # create DNAT rule
    nat_dnat:
        cloud: otc
        nat_gateway: 2b725feb-f0b7-4dcc-a7b4-e02336867123
        internal_service_port: 80
        external_service_port: 80
        port: 840bbea5-aaf8-40b9-bf17-cc081a785123
        floating_ip: f39ef6e6-a4b3-42be-a501-b7dfe251b123
        protocol: tcp
        state: present



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>dnat_rule</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                    </div>
                </td>
                <td>On Success.</td>
                <td>
                            <div>List of dictionaries describing DNAT rules.</div>
                    <br/>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>admin_state_up</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>Specifies whether the rule is active or down.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>created_at</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>Creation time of the DNAT rule</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">yyyy-mm-dd hh:mm:ss</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>external_service_port</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>Specifies the port for providing external services.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">80</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>floating_ip</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>IP / ID of the floating IP Address assigned to the rule.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">123.12.1.12</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>ID of the DNAT rule</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">5acab424-69fb-4408-93d1-b2801b306827</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>internal_service_port</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>Specifies the port used by ECSs or BMSs to provide services for external systems</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">80</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>nat_gateway_id</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>ID or name of the assigned Nat gateway.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2aa32feb-f0b7-4dcc-a7b4-e0233686702b</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>Specifies the port ID of an ECS or a BMS. This parameter and private_ip are alternative</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">736abea5-aaf8-40b9-bf17-cc081a785d67</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>private_ip</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>Specifies the private IP address, e.g. the IP address of a Direct Connect connection. This parameter and port are alternative</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">192.168.2.1</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>Used protocol</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">tcp</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td></td>
                <td>
                            <div>Specifies the status of the NAT gateway.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACTIVE</div>
                </td>
            </tr>

    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Sebastian Gode (@SebastianGode)
