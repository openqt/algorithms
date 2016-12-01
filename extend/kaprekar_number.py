# coding=utf-8
"""
卡布列克数
http://group.jobbole.com/26887/

有一种数被称为卡布列克数，其形式如：45 * 45 = 2025 并且 20+25=45，这样 45 就是一个
卡布列克数。

它标准定义如下：

    若正整数X在N进制下的平方可以分割为二个数字，而这二个数字相加后恰等于X，那么X就是
    N进制下的卡布列克数。
    分解后的数字必须是正整数才可以，例如：10*10=100 并且 10+0=10，因为0不是正整数，
    所以10不是卡布列克数。

现在题目的要求是给定你一个范围[a,b]（b大于等于a，a大于等于0），你需要把这个范围内的
卡布列克数全部输出。

样例如下：
    输入：2 100
    输出：9 45 55 99
"""
from __future__ import print_function


def is_kaprekar(n):
    level, sq = 10, n * n
    while level < sq:
        a, b = divmod(sq, level)
        if b > 0 and a + b == n:
            return level
        level *= 10
    return 0


def kaprekar_number(start, stop=None):
    while True:
        if is_kaprekar(start):
            yield start

        if stop and start >= stop:
            break
        start += 1


if __name__ == '__main__':
    print(is_kaprekar(45))
    print(is_kaprekar(40))
    print(is_kaprekar(100))
    print([i for i in kaprekar_number(2, 1000)])
