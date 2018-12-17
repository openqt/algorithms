#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
import logging
import os
from os import path
import traceback
import sys

logging.basicConfig(level=logging.WARN)


###
# - [x] 指定目录做文件提升的操作
# - [ ] 遍历目录做提升操作
# - [ ] 提供一个基于装饰器的参数设置功能及支持定制化功能
###

class UpOneLevel(object):
    """ 找到所有的叶子节点并且做一次文件提升操作



    """

    def __init__(self):
        pass

    def show_exception(self):
        etype, value, tb = sys.exc_info()
        msg = traceback.format_exception(etype, value, tb)
        print(" > ", msg[-1])

    def renfile(self, old, new):
        try:
            os.rename(old, new)
            return True
        except:
            self.show_exception()
        return False

    def upfiles(self, topdir):
        """将文件提升一级目录，按照`<目录名>.<文件名>`的方式重命名提升的新的文件

        """
        topdir = path.normpath(topdir)  # 规范化路径以备后继处理
        upname = path.basename(topdir)  # 分解当前路径，提升用
        print("In %s" % topdir)

        num = 0
        try:
            for name in os.listdir(topdir):  # 遍历当前目录
                oldfile = path.join(topdir, name)  # 合成全路径
                if not path.isfile(oldfile):  # 非文件类型不处理
                    logging.info("Ignoring non-file: %s", oldfile)
                    continue

                newname = "%s.%s" % (upname, name)
                newfile = path.abspath(path.join(topdir, '..', newname))
                print("%s => %s" % (oldfile, newfile))

                if self.renfile(oldfile, newfile):
                    num += 1
                logging.info("Up %s file(s) from %s.", num, topdir)

            print("Delete %s" % topdir)
            os.rmdir(topdir)
        except:
            self.show_exception()

        return num

    def walk(self, path):
        """遍历路径，给出所有需要提升文件的路径集合"""

        for root, dirs, files in os.walk(path):
            if not dirs:  # 无子目录
                pass



def main():
    up = UpOneLevel()
    logging.debug("Current %s" % os.getcwd())

    # up.upfiles("/tmp/t/t")
    top = sys.argv[1]
    up.upfiles(top)


if __name__ == '__main__':
    main()
