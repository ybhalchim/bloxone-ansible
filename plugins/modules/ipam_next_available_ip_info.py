#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_next_available_ip_info
short_description: Manage Address
description:
    - Manage Address
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - "ID of the object."
        type: str
        required: true
    contiguous:
        description:
            - "Indicates whether the IP addresses should belong to a contiguous block. Defaults to false."
        type: bool
        required: false
    count:
        description:
            - "The number of IP addresses requested. Defaults to 1."
        type: int
        required: false
            

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: Get Information about Next Available IP in Address Block
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _address_block.id }}"
        count: 5

    - name: Get Information about Next Available IP in Address Block Default Count
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _address_block.id }}"

    - name: Get Information about Next Available IP in Subnet
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _subnet.id }}"
        count: 5

    - name: Get Information about Next Available IP in Subnet Default Count
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _subnet.id }}"
        
    - name: Get Information about Next Available IP in Range
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _range.id }}"
        count: 5
        
    - name: Get Information about Next Available IP in Range Default Count
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _range.id }}"
   
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the Address object
    type: str
    returned: Always
objects:
    description:
        - Address object
    type: list
    elements: dict
    returned: Always
    contains:
        address:
            description:
                - "The address in form \"a.b.c.d\"."
            type: str
            returned: Always
        comment:
            description:
                - "The description for the address object. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        compartment_id:
            description:
                - "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        dhcp_info:
            description:
                - "The DHCP information associated with this object."
            type: dict
            returned: Always
            contains:
                client_hostname:
                    description:
                        - "The DHCP host name associated with this client."
                    type: str
                    returned: Always
                client_hwaddr:
                    description:
                        - "The hardware address associated with this client."
                    type: str
                    returned: Always
                client_id:
                    description:
                        - "The ID associated with this client."
                    type: str
                    returned: Always
                end:
                    description:
                        - "The timestamp at which the I(state), when set to I(leased), will be changed to I(free)."
                    type: str
                    returned: Always
                fingerprint:
                    description:
                        - "The DHCP fingerprint for the associated lease."
                    type: str
                    returned: Always
                iaid:
                    description:
                        - "Identity Association Identifier (IAID) of the lease. Applicable only for DHCPv6."
                    type: int
                    returned: Always
                lease_type:
                    description:
                        - "Lease type. Applicable only for address under DHCP control. The value can be empty for address not under DHCP control."
                        - "Valid values are:"
                        - "* I(DHCPv6NonTemporaryAddress): DHCPv6 non-temporary address (NA)"
                        - "* I(DHCPv6TemporaryAddress): DHCPv6 temporary address (TA)"
                        - "* I(DHCPv6PrefixDelegation): DHCPv6 prefix delegation (PD)"
                        - "* I(DHCPv4): DHCPv4 lease"
                    type: str
                    returned: Always
                preferred_lifetime:
                    description:
                        - "The length of time that a valid address is preferred (i.e., the time until deprecation). When the preferred lifetime expires, the address becomes deprecated on the client. It is still considered leased on the server. Applicable only for DHCPv6."
                    type: str
                    returned: Always
                remain:
                    description:
                        - "The remaining time, in seconds, until which the I(state), when set to I(leased), will remain in that state."
                    type: int
                    returned: Always
                start:
                    description:
                        - "The timestamp at which I(state) was first set to I(leased)."
                    type: str
                    returned: Always
                state:
                    description:
                        - "Indicates the status of this IP address from a DHCP protocol standpoint as:"
                        - "* I(none): Address is not under DHCP control."
                        - "* I(free): Address is under DHCP control but has no lease currently assigned."
                        - "* I(leased): Address is under DHCP control and has a lease currently assigned. The lease details are contained in the matching I(dhcp/lease) resource."
                    type: str
                    returned: Always
                state_ts:
                    description:
                        - "The timestamp at which the I(state) was last reported."
                    type: str
                    returned: Always
        disable_dhcp:
            description:
                - "Read only. Represent the value of the same field in the associated I(dhcp/fixed_address) object."
            type: bool
            returned: Always
        discovery_attrs:
            description:
                - "The discovery attributes for this address in JSON format."
            type: dict
            returned: Always
        discovery_metadata:
            description:
                - "The discovery metadata for this address in JSON format."
            type: dict
            returned: Always
        external_keys:
            description:
                - "The external keys (source key) for this address in JSON format."
            type: dict
            returned: Always
        host:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        hwaddr:
            description:
                - "The hardware address associated with this IP address."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        interface:
            description:
                - "The name of the network interface card (NIC) associated with the address, if any."
            type: str
            returned: Always
        names:
            description:
                - "The list of all names associated with this address."
            type: list
            returned: Always
            elements: dict
            contains:
                name:
                    description:
                        - "The name expressed as a single label or FQDN."
                    type: str
                    returned: Always
                type:
                    description:
                        - "The origin of the name."
                    type: str
                    returned: Always
        parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        protocol:
            description:
                - "The type of protocol (I(ip4) or I(ip6))."
            type: str
            returned: Always
        range:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        space:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        state:
            description:
                - "The state of the address (I(used) or I(free))."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for this address in JSON format."
            type: dict
            returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        usage:
            description:
                - "The usage is a combination of indicators, each tracking a specific associated use. Listed below are usage indicators with their meaning: usage indicator        | description ---------------------- | -------------------------------- I(IPAM)                 |  Address was created by the IPAM component. I(IPAM), I(RESERVED)     |  Address was created by the API call I(ipam/address) or I(ipam/host). I(IPAM), I(NETWORK)      |  Address was automatically created by the IPAM component and is the network address of the parent subnet. I(IPAM), I(BROADCAST)    |  Address was automatically created by the IPAM component and is the broadcast address of the parent subnet. I(DHCP)                 |  Address was created by the DHCP component. I(DHCP), I(FIXEDADDRESS) |  Address was created by the API call I(dhcp/fixed_address). I(DHCP), I(LEASED)       |  An active lease for that address was issued by a DHCP server. I(DHCP), I(DISABLED)     |  Address is disabled. I(DNS)                  |  Address is used by one or more DNS records. I(DISCOVERED)           |  Address is discovered by some network discovery probe like Network Insight or NetMRI in NIOS."
            type: list
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException
    from ipam import AddressBlockApi, RangeApi, SubnetApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class NextAvailableIPInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(NextAvailableIPInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find(self):

        all_results = []
        offset = 0

        while True:
            try:
                id = self.params["id"]
                address_str = id.rsplit("/", 1)[0]
                if address_str == "ipam/address_block":
                    resp = AddressBlockApi(self.client).list_next_available_ip(
                        id=id, contiguous=self.params["contiguous"], count=self.params["count"]
                    )
                elif address_str == "ipam/subnet":
                    resp = SubnetApi(self.client).list_next_available_ip(
                        id=id, contiguous=self.params["contiguous"], count=self.params["count"]
                    )

                elif address_str == "ipam/range":
                    resp = RangeApi(self.client).list_next_available_ip(
                        id=id, contiguous=self.params["contiguous"], count=self.params["count"]
                    )

                all_results.extend(resp.results)

                if len(resp.results) < self._limit:
                    break
                offset += self._limit

            except ApiException as e:
                self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        return all_results

    def run_command(self):
        result = dict(objects=[])

        if self.check_mode:
            self.exit_json(**result)

        find_results = self.find()

        all_results = []
        for r in find_results:
            all_results.append(r.model_dump(by_alias=True, exclude_none=True))

        result["objects"] = all_results
        self.exit_json(**result)


def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        id=dict(type="str", required=True),
        contiguous=dict(type="bool", required=False),
        count=dict(type="int", required=False),
    )

    module = NextAvailableIPInfoModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    module.run_command()


if __name__ == "__main__":
    main()
