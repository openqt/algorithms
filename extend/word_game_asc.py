# coding=utf-8
"""
一道腾讯面试题的思考：到底谁会赢
http://geekori.cn/archives/151

有甲乙两家伙用一个英语单词玩游戏（无聊的人还是很多的！！！）。两个人轮流进行，每个人
每次从中删掉任意一个字母，如果剩余的字母序列是严格单调递增的（按字典序
a < b < c <….<z，假设单词字母不区分大小写，也就是说，a与A算相等），则这个人胜利。
假设两个人都足够聪明（即如果有赢的方案，都不会选输的方案 ），甲先开始，问他能赢么？

    输入： 一连串英文小写字母，长度任意（当然要在计算机能承受的范围内）,保证最开始的
    状态不是一个严格单增的序列。
    输出：1表示甲可以赢，0表示甲不能赢。

    例如: 输入 bad， 则甲可以删掉b或者a,剩余的是ad或者bd，他就赢了，输出1。
    又如: 输入 aaa， 则甲只能删掉1个a，乙删掉一个a,剩余1个a，乙获胜，输出0。
"""
from __future__ import print_function
