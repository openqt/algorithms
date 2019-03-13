#!/usr/bin/env python3
# coding=utf-8
import glob
import re
import sys
import time
import unicodedata
from string import Template

import html2text
import requests
from readability import Document

python_template = u'''#!/usr/bin/env python
# coding=utf-8

"""$id. $title
$url

$text
"""
'''


def slugify(string):
    """
    Slugify a unicode string.
    """
    s = unicodedata.normalize('NFKD', string).strip()
    return re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', s).lower())


class PE(object):
    def __init__(self):
        self.sess = requests.session()
        self.url = None
        self.id = 0
        self.html = None

    @property
    def title(self):
        match = re.search(r"<h2>(.*)?</h2>", self.html)
        return match.group(1).strip()

    @property
    def filename(self):
        return "pe%03d-%s.py" % (self.id, slugify(self.title))

    def get(self, id, bypass_existed=True):
        self.id = int(id)
        self.html = None
        if bypass_existed:
            files = glob.glob("pe%03d-*.py" % self.id)
            if files:
                print("|", *files)
                return self
        self.url = "https://projecteuler.net/problem={}".format(self.id)

        resp = self.sess.get(verify=True, url=self.url)
        resp.raise_for_status()
        self.html = resp.text
        return self

    def save(self):
        if not self.html:
            return False

        doc = Document(self.html)
        text = html2text.HTML2Text().handle(doc.summary()).strip()

        kwargs = {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "text": text,
        }
        code = Template(python_template).substitute(**kwargs).encode("utf-8")
        with open(self.filename, "wb") as f:
            f.write(code)
        print(">", self.filename)
        return True


def main():
    pe = PE()
    if len(sys.argv) > 1:
        argv = sys.argv[1:]
    else:
        argv = range(1, 661)

    for i in argv:
        if pe.get(i).save():
            time.sleep(.2)


if __name__ == "__main__":
    main()
