#!/usr/bin/env python
# coding=utf-8
import argparse
import json
import logging
import os
import time
from string import Template

import prettytable
import requests
import html2text

logging.basicConfig(level=logging.WARN)

python_template = u'''# coding=utf-8
import unittest

"""$id. $title
$url

$text


Similar Questions:
$related
"""


$code

class T(unittest.TestCase):
    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
'''

golang_template = u'''package main

import (
    "fmt"
)

/*$id. $title
$url

$text


Similar Questions:
$related
*/
$code

func main() {
    fmt.Println()
}
'''

Q_getQuestionDetail = """
query getQuestionDetail($titleSlug: String!) {
  isCurrentUserAuthenticated
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    questionTitle
    translatedTitle
    questionTitleSlug
    content
    translatedContent
    difficulty
    allowDiscuss
    similarQuestions
    mysqlSchemas
    categoryTitle
    codeDefinition
    metaData
    infoVerified
    envInfo
    article
    questionDetailUrl
    libraryUrl
    topicTags {
      name
      slug
      translatedName
    }
  }
  isPremium
}"""


class Question(object):
    def __init__(self, **kwargs):
        self.filter = html2text.HTML2Text()  # from html to markdown
        self.data = None  # response origin json response

        stat = kwargs.get("stat")
        if stat:
            self.qid = stat.get("frontend_question_id")
            self.title = stat.get("question__title")
            self.slug = stat.get("question__title_slug")
        self.url = "https://leetcode.com/problems/{}/description/".format(self.slug)

        self.paid = kwargs.get("paid_only", False)  # premium problems
        self.content = None  # problem description
        self.related = None  # related problem list
        self.codes = {}  # code template for a problem

        self.loaded = False  # the problem is load from file or download from internet

        difficulty = kwargs.get("difficulty")
        self.level = difficulty.get("level", 0)

    def name(self):
        return "lc%03d-%s" % (self.qid, self.slug)

    def metaname(self):
        return self.name() + ".json"

    def code(self, language="python,golang"):
        for lang in language.split(","):
            self._code(lang)

    def _code(self, language="python"):
        if not self.data:
            logging.info("No DATA")
            return

        if language not in self.codes:
            print("Supported language: {}".format(self.codes.keys()))
            return

        if not self.loaded:  # loaded json not write-back
            with open(self.metaname(), "w") as f:
                json.dump(self.data, f, indent=2)

        kwargs = {
            "id": self.qid,
            "title": self.title,
            "url": self.url,
            "text": self.content,
            "code": self.codes[language],
            "related": "\n".join(["  " + i for i in self.related]),
        }

        if language == "python":
            text = Template(python_template).substitute(**kwargs).encode("utf-8")

            filename = self.name() + ".py"
            with open(filename, "w") as f:
                f.write(text)
            print("{} generated".format(filename))
        elif language == "golang":
            text = Template(golang_template).substitute(**kwargs).encode("utf-8")

            filename = self.name() + ".go"
            with open(filename, "w") as f:
                f.write(text)
            print("{} generated".format(filename))
        else:
            print("Not support language: {}".format(language))

    def sort(self, data):
        self.data = data
        try:
            question = self.data["question"]
            for code in json.loads(question["codeDefinition"]):
                self.codes[code["value"]] = code["defaultCode"]
            self.content = self.filter.handle(question["content"]).strip()
            self.related = []
            for sq in json.loads(question["similarQuestions"]):
                self.related.append("{} ({})".format(sq["title"], sq["titleSlug"]))
        except Exception as exc:
            logging.error("{}: {}, {}".format(exc, self.title, self.url))

    def load(self, filename):
        with open(filename) as f:
            self.sort(json.load(f))
        self.loaded = True
        logging.debug("Load {} OK".format(filename))


class LC(object):
    def __init__(self):
        self.sess = requests.session()

        self.url = "https://leetcode.com/api/problems/algorithms/"
        self.qa = []
        self.qm = {}
        self.arg = None
        self.data = None

    def args(self):
        p = argparse.ArgumentParser()
        p.add_argument("--lang", default="python,golang",
                       help="Generate specific language code, default is python and golang")
        p.add_argument("--reload", action="store_true",
                       help="Load cached list and regenerate all problems")
        p.add_argument("--noshow", action="store_true", help="Not show problems")
        p.add_argument("--nocode", action="store_true", help="Not generate code")
        p.add_argument("problems", nargs="*", help="Problems' slug name")
        self.arg = p.parse_args()

    def list(self):
        resp = self.sess.get(self.url)
        resp.raise_for_status()

        self.data = resp.json()
        self.__sort_data()

    def __sort_data(self):
        logging.debug(self.data.get("category_slug"))
        logging.debug("num_total {}".format(self.data.get("num_total")))

        for status in self.data["stat_status_pairs"]:
            q = Question(**status)
            self.qa.append(q)
            self.qm[q.slug] = q

            # 删除不重要的变量值
            status['stat'].pop('total_acs')
            status['stat'].pop('total_submitted')

    def show(self):
        pt = prettytable.PrettyTable(["ID", "Title", "Level", "Paid"])
        pt.align["Title"] = "l"
        for i in self.qa:
            pt.add_row([i.qid, i.title, i.level, "X" if i.paid else " "])
        print(pt)
        print("Total: {}".format(len(self.qa)))

    def save(self, filename):
        if self.data:
            with open(filename, "w") as f:
                json.dump(self.data, f, indent=2)

    def load(self, filename):
        with open(filename) as f:
            self.data = json.load(f)
        self.__sort_data()

    def detail(self, q):
        if q.paid:
            logging.info("Ignoring paid question {}({})".format(q.title, q.slug))
            return False

        if os.path.exists(q.metaname()):
            q.load(q.metaname())
        else:
            print("Pulling {}: {}".format(q.qid, q.title))

            if not self.sess.cookies.get("csrftoken"):
                self.sess.get(q.url)

            body = {
                "operationName": "getQuestionDetail",
                "variables": {"titleSlug": q.slug},
                "query": Q_getQuestionDetail,
            }
            self.sess.headers["referer"] = q.url
            self.sess.headers["x-csrftoken"] = self.sess.cookies["csrftoken"]
            resp = self.sess.post("https://leetcode.com/graphql", json=body)
            if resp.status_code >= 400:
                logging.error(resp.content)
                resp.raise_for_status()

            q.sort(resp.json().get("data"))
            time.sleep(.5)
        return True


def code_generation(lc):
    if lc.arg.problems:
        for slug in lc.arg.problems:
            q = lc.qm.get(slug)
            if q:
                lc.detail(q)
                q.code(lc.arg.lang)
            else:
                print("Not found {}".format(slug))
    else:
        for q in lc.qa:
            if lc.detail(q) and lc.arg.reload or not q.loaded:
                q.code(lc.arg.lang)


def main():
    lc = LC()
    lc.args()

    if lc.arg.reload:
        lc.load("leetcode.json")

    if not lc.data:
        lc.list()
        lc.save("leetcode.json")

    if not lc.arg.noshow:
        lc.show()

    if not lc.arg.nocode:
        code_generation(lc)


if __name__ == "__main__":
    main()
