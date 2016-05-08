#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        address_block_list = self.restoreAddress(s, 1)
        address_list = []
        for address in address_block_list:
            if len(address) == 4:
                address_list.append(".".join(address))
        return address_list

    def restoreAddress(self, s, count):
        address_block = []
        # No address field
        if not s:
            return address_block

        # We have get the fourth address fields
        if count == 4:
            if s[0] != "0" and len(s) <= 3 and int(s) <= 255:
                address_block.append([s])
            if s == "0":
                address_block.append([s])
            return address_block

        # Current field is '0'
        if s[0] == "0":
            address_1 = self.restoreAddress(s[1:], count + 1)
            for block in address_1:
                cur_address = ['0']
                cur_address.extend(block)
                if len(cur_address) == 5 - count:
                    address_block.append(cur_address)
            return address_block

        # Current address field is made by i numbers.
        for i in range(1, 4):
            if len(s) < i or int(s[:i]) > 255:
                continue
            address_1 = self.restoreAddress(s[i:], count + 1)
            for block in address_1:
                cur_address = [s[:i]]
                cur_address.extend(block)
                if len(cur_address) == 5 - count:
                    address_block.append(cur_address)
        return address_block

"""
"25525511135"
"0000"
"0100100"
"11"
"""
