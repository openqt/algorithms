#!/usr/bin/env python
import argparse
import json
import logging
import os
import time
from string import Template

import prettytable
import requests
import html2text


logging.basicConfig(level=logging.INFO)

python_template = u'''# coding=utf-8
import unittest

"""$id. $title
$url

$text


Similar Questions:
$related
"""


$code

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
    stats
    allowDiscuss
    contributors
    similarQuestions
    mysqlSchemas
    randomQuestionUrl
    sessionId
    categoryTitle
    submitUrl
    interpretUrl
    codeDefinition
    sampleTestCase
    enableTestMode
    metaData
    enableRunCode
    enableSubmit
    judgerAvailable
    infoVerified
    envInfo
    urlManager
    article
    questionDetailUrl
    libraryUrl
    topicTags {
      name
      slug
      translatedName
      __typename
    }
    __typename
  }
  subscribeUrl
  isPremium
  loginUrl
}"""


class Question(object):
    def __init__(self, **kwargs):
        self.filter = html2text.HTML2Text()
        self.data = None

        stat = kwargs.get("stat")
        if stat:
            self.qid = stat.get("frontend_question_id")
            self.title = stat.get("question__title")
            self.slug = stat.get("question__title_slug")
        self.url = "https://leetcode.com/problems/{}/description/".format(self.slug)

        self.paid = kwargs.get("paid_only", False)
        self.content = None
        self.related = None
        self.codes = {}

        difficulty = kwargs.get("difficulty")
        self.level = difficulty.get("level", 0)

    def name(self):
        return "lc%03d-%s" % (self.qid, self.slug)

    def metaname(self):
        return self.name() + ".json"

    def code(self, language="python"):
        if language not in self.codes:
            print("Supported language: {}".format(self.codes.keys()))
            return

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
        except:
            logging.error("{}, {}".format(self.title, self.url))

    def load(self, filename):
        with open(filename) as f:
            self.sort(json.load(f))
        print("Load {} OK".format(filename))


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
        p.add_argument("--lang", default="python", help="Generate specific language code, default is python")
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
            print("Ignoring paid question {}({})".format(q.title, q.slug))
            return

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
            resp.raise_for_status()
            q.sort(resp.json().get("data"))
            time.sleep(.5)


def main():
    lc = LC()
    lc.args()
    # lc.list()

    lc.load("leetcode.json")
    # lc.show()
    # lc.save("leetcode.json")

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
            lc.detail(q)
            q.code(lc.arg.lang)


if __name__ == "__main__":
    main()
