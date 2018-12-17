#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function

import argparse
import logging
import os
import sys
import traceback
from os import path

ap = argparse.ArgumentParser(description="Move files up/down folders")
ap.add_argument("topdir", nargs="*", default=".", help="Top (root) path")

logging.basicConfig(level=logging.WARN)


def Arg(*a, **ka):
    """简化的参数配置"""
    ap.add_argument(*a, **ka)

    def _func(func):
        def _args(*args, **kwargs):
            return func(*args, **kwargs)

        return _args

    return _func


def show_exception():
    """显示简要的错误信息"""
    etype, value, tb = sys.exc_info()
    msg = traceback.format_exception(etype, value, tb)
    print(" > ", msg[-1])


class StepFiles(object):
    """ 找到所有的叶子节点并且做一次文件提升操作

    - [x] 指定目录做文件提升的操作
    - [x] 遍历目录做提升操作
    - [x] 提供一个基于装饰器的参数设置功能及支持定制化功能

    """

    def __init__(self):
        pass

    def __renfile(self, old, new):
        """重命名文件，处理异常
        :param old: 原始文件名
        :param new: 改名后的文件名
        :return: 成功/失败
        """
        try:
            os.rename(old, new)
            return True
        except:
            show_exception()
        return False

    def upfiles(self, topdir):
        """将文件提升一级目录，按照`<目录名>.<文件名>`的方式重命名提升的新的文件
        :param topdir: 起始文件夹
        :return: 成功改名的文件数量

        """
        topdir = path.normpath(topdir)  # 规范化路径以备后继处理
        upname = path.basename(topdir)  # 分解当前路径，提升用
        logging.debug("In %s" % topdir)

        num = 0
        for name in os.listdir(topdir):  # 遍历当前目录
            oldfile = path.join(topdir, name)  # 合成全路径
            if not path.isfile(oldfile):  # 非文件类型不处理
                logging.info("Ignoring non-file: %s", oldfile)
                continue

            newname = "%s.%s" % (upname, name)
            newfile = path.abspath(path.join(topdir, '..', newname))
            print("%s => %s" % (oldfile, newfile))  # 显示改名前后信息

            if self.__renfile(oldfile, newfile):
                num += 1  # 改名成功记录一次
            logging.info("Up %s file(s) from %s.", num, topdir)

        print("Delete %s" % topdir)
        os.rmdir(topdir)

        return num

    def walk(self, topdir):
        """遍历路径，给出所有叶子节点

        """
        logging.info("Start from %s" % topdir)
        for root, dirs, files in os.walk(topdir):
            if not dirs:  # 无子目录
                yield root

    def downfiles(self, topdir):
        """将文件按文件名规则下发到各个子目录"""
        print("Not implemented.")


def up(topdir):
    """上移文件"""
    step = StepFiles()
    ok = False
    try:
        for i in step.walk(topdir):
            ok = True
            step.upfiles(i)
    except:
        show_exception()
    return ok


def down(topdir):
    """下移文件"""
    step = StepFiles()
    ok = False
    try:
        for i in step.walk(topdir):
            ok = True
            step.downfiles(i)
    except:
        show_exception()
    return ok


@Arg("-a", "--all", action='store_true', help="Move all files until top directory")
@Arg("--down", action='store_true', help="Move files down to folder (default is up)")
def main(**kwargs):
    """主函数入口"""
    logging.debug("Current %s" % os.getcwd())

    argv = ap.parse_args()
    print(argv)

    def _logic(func):
        if argv.all:
            while func(topdir): pass
        else:
            func(topdir)

    for topdir in argv.topdir:
        if argv.down:
            _logic(down)
        else:
            _logic(up)


if __name__ == '__main__':
    main()
