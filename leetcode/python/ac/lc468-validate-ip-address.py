# coding=utf-8
import unittest

"""468. Validate IP Address
https://leetcode.com/problems/validate-ip-address/description/

Write a function to check whether an input string is a valid IPv4 address or
IPv6 address or neither.

**IPv4** addresses are canonically represented in dot-decimal notation, which
consists of four decimal numbers, each ranging from 0 to 255, separated by
dots ("."), e.g.,`172.16.254.1`;

Besides, leading zeros in the IPv4 is invalid. For example, the address
`172.16.254.01` is invalid.

**IPv6** addresses are represented as eight groups of four hexadecimal digits,
each group representing 16 bits. The groups are separated by colons (":"). For
example, the address `2001:0db8:85a3:0000:0000:8a2e:0370:7334` is a valid one.
Also, we could omit some leading zeros among four hexadecimal digits and some
low-case characters in the address to upper-case ones, so
`2001:db8:85a3:0:0:8A2E:0370:7334` is also a valid IPv6 address(Omit leading
zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single
empty group using two consecutive colons (::) to pursue simplicity. For
example, `2001:0db8:85a3::8A2E:0370:7334` is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the
address `02001:0db8:85a3:0000:0000:8a2e:0370:7334` is invalid.

**Note:** You may assume there is no extra space or special characters in the
input string.

**Example 1:**  

    
    
    **Input:** "172.16.254.1"
    
    **Output:** "IPv4"
    
    **Explanation:** This is a valid IPv4 address, return "IPv4".
    

**Example 2:**  

    
    
    **Input:** "2001:0db8:85a3:0:0:8A2E:0370:7334"
    
    **Output:** "IPv6"
    
    **Explanation:** This is a valid IPv6 address, return "IPv6".
    

**Example 3:**  

    
    
    **Input:** "256.256.256.256"
    
    **Output:** "Neither"
    
    **Explanation:** This is neither a IPv4 address nor a IPv6 address.


Similar Questions:
  IP to CIDR (ip-to-cidr)
"""

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self._ipv4(IP): return "IPv4"
        if self._ipv6(IP): return "IPv6"
        return "Neither"

    def _ipv4(self, s):
        try:
            groups = s.split('.')
            if len(groups) != 4: return False  # 不是4个组
            for group in groups:
                if not group.isdigit(): return False  # 不是数字，包括有+/-符号
                if len(group) > 1:
                    if group[0] == '0': return False  # 前面不能有额外的0
                    if not (0 <= int(group) <= 255):  # 必须小于255
                        return False
        except:
            return False
        return True

    def _ipv6(self, s):
        try:
            groups = s.split(':')
            if len(groups) != 8: return False  # 不是8个组
            for group in groups:
                if len(group) > 4 or not group.isalnum(): return False
                int(group, 16)
        except:
            return False
        return True


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.validIPAddress("0.0.0.-0"), "Neither")
        self.assertEqual(s.validIPAddress("00.0.0.0"), "Neither")
        self.assertEqual(s.validIPAddress("1.0.1."), "Neither")
        self.assertEqual(s.validIPAddress("01.01.01.01"), "Neither")
        self.assertEqual(s.validIPAddress("172.16.254.1"), "IPv4")
        self.assertEqual(s.validIPAddress("256.256.256.256"), "Neither")
        self.assertEqual(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"), "IPv6")
        self.assertEqual(s.validIPAddress("02001:0db8:85a3:0:0:8A2E:0370:7334"), "Neither")
        self.assertEqual(s.validIPAddress("1081:db8:85a3:01:-0:8A2E:0370:7334"), "Neither")


if __name__ == "__main__":
    unittest.main()
