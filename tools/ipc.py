#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function

import argparse
import functools
import re


def Arg(*args, **kwargs):
    """简化的参数配置"""
    parser = getattr(Arg, 'parser', None)
    if not parser:  # 将参数解析放到函数属性内
        parser = argparse.ArgumentParser(description="ove files up/down folders")
        parser.add_argument("ip", nargs="*", help="Top (root) path")

        Arg.parser = parser

    def _func(func):
        parser.add_argument(*args, **kwargs)

        @functools.wraps(func)
        def _args(*_args, **_kwargs):
            return func(*_args, **_kwargs)

        return _args

    return _func


class IP(object):
    cidr_rule = re.compile(r'^\d+\.\d+\.\d+\.\d+/\d+$')
    addr_rule = re.compile(r'^\d+\.\d+\.\d+\.\d+$')

    def __init__(self, ip=None, mask=None):
        self._addr = bytearray(4)
        self._mask = bytearray(4)

        if ip:
            if mask:
                self.addr, self.mask = ip, mask
            else:
                self.addr, self.cidr = ip.split('/', 1)

    @property
    def cidr(self):
        """子网掩码转换为CIDR数值"""
        val = 0
        for m in self._mask:
            while m > 0:
                val += 1
                m &= m - 1
        return val

    @cidr.setter
    def cidr(self, s):
        """设置CIDR指定子网掩码"""
        self._mask = bytearray(4)
        if not s:
            return

        a, b = divmod(int(s), 8)
        for i in range(a):
            self._mask[i] = 0xFF

        if a < 4:  # /32
            self._mask[a] = 0xFF << (8 - b) & 0xFF

    @property
    def mask(self):
        """子网掩码表示"""
        return self.tostr(self._mask)

    @mask.setter
    def mask(self, s):
        """子网掩码字符表示转为内部结构"""
        if not IP.addr_rule.match(s):
            return
        for n, i in enumerate(s.split('.')):
            self._mask[n] = int(i)

    @property
    def addr(self):
        return ".".join(str(i) for i in self._addr)

    @addr.setter
    def addr(self, s):
        """各种格式IP地址转换"""
        self._addr = bytearray(4)
        if not s:
            return

        _addr = None
        if isinstance(s, (list, tuple)) and len(s) == 4:
            # 列表表示
            _addr = [int(i) for i in s]
        elif isinstance(s, (str, unicode)):
            if s.count('.') == 3:  # .分隔的字符串表示
                _addr = [int(i) for i in s.split('.')]
            elif len(s) == 12:  # 无.分隔的字符串表示
                _addr = [int(s[i:i + 3]) for i in range(0, 12, 3)]
        elif isinstance(s, (int, long)):
            # 大整数表示
            _addr = []
            for i in range(4):
                _addr.append(s % 1000)
                s /= 1000
            _addr.reverse()

        if _addr:
            for n, i in enumerate(_addr):
                self._addr[n] = i

    def binmask(self, data):
        """二进制表示法"""
        s = ""
        for i in data:
            s += "{:08b} ".format(i)
        return s[:-1]

    @property
    def min_range(self):
        """网络IP最小值"""
        val = []
        for i in range(4):
            val.append(self._addr[i] & self._mask[i])
        return self.tostr(val)

    @property
    def max_range(self):
        """网络IP最大值"""
        val = []
        for i in range(4):
            addr = self._addr[i] & self._mask[i]
            revmask = self._mask[i] ^ 0xFF
            val.append(addr | revmask)
        return self.tostr(val)

    def tostr(self, l):
        """列表转.分隔的字符串"""
        return ".".join(str(i) for i in l)

    def show(self):
        print("CIDR: %s/%d" % (self.addr, self.cidr))
        print("MASK: %s" % self.mask)
        print("RANGE: (%s, %s)" % (self.min_range, self.max_range))
        print()

        print("ADDR: %s" % self.binmask(self._addr))
        print("MASK: %s" % self.binmask(self._mask).replace('0', '-'))
        print()


@Arg("-a", "--auto", action='store_true', help="Calculate IP Address by local device")
def main():
    """主函数入口"""
    argv = Arg.parser.parse_args()
    if len(argv.ip) == 2 and not IP.cidr_rule.match(argv.ip[0]):
        ip = IP(*argv.ip)
        ip.show()
        exit(0)

    for ip in argv.ip:
        if IP.cidr_rule.match(ip):
            ip = IP(ip)
            ip.show()
        else:
            print("%s malformed." % ip)


if __name__ == '__main__':
    main()
