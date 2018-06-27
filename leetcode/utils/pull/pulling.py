#!/usr/bin/env python
import argparse
import json
import logging
import time
from string import Template

import prettytable
import requests

logging.basicConfig(level=logging.INFO)

python_template = u'''# coding=utf-8
import unittest

"""$title
$url

$text
"""


$code

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
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
        self.data = None

        stat = kwargs.get("stat")
        if stat:
            self.qid = stat.get("frontend_question_id")
            self.title = stat.get("question__title")
            self.slug = stat.get("question__title_slug")
        self.url = "https://leetcode.com/problems/{}/description/".format(self.slug)

        self.paid = kwargs.get("paid_only", False)
        self.content = None
        self.codes = {}

        difficulty = kwargs.get("difficulty")
        self.level = difficulty.get("level", 0)

    def code(self, language="python"):
        if language not in self.codes:
            print("Supported language: {}".format(self.codes.keys()))
            return

        text = Template(python_template).substitute(
            title=self.title,
            url=self.url,
            text=self.content,
            code=self.codes[language]).encode("utf-8")

        name = "lc%03d-%s" % (self.qid, self.slug)
        with open(name + ".py", "w") as f:
            f.write(text)

        with open(name + ".json", "w") as f:
            json.dump(self.data, f, indent=2)

    def sort(self, data):
        self.data = data
        question = self.data["question"]
        for code in json.loads(question["codeDefinition"]):
            self.codes[code["value"]] = code["defaultCode"]
        self.content = question["content"]


class LC(object):
    def __init__(self):
        self.url = "https://leetcode.com/api/problems/algorithms/"
        self.sess = requests.session()
        self.qa = []
        self.qm = {}
        self.arg = None
        self.data = None

    def args(self):
        p = argparse.ArgumentParser()
        p.add_argument("--code", help="Generate specific language code.")
        self.arg = p.parse_args()

    def list(self):
        resp = self.sess.get(self.url)
        resp.raise_for_status()

        self.data = resp.json()
        self.__sort_data()

    def __sort_data(self):
        logging.info(self.data.get("category_slug"))
        logging.info("num_total {}".format(self.data.get("num_total")))

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


def main():
    lc = LC()
    lc.args()
    # lc.list()

    lc.load("leetcode.json")
    # lc.show()
    # lc.save("leetcode.json")

    # q = lc.qm["exam-room"]
    # lc.detail(q)
    # q.code()

    for q in lc.qa:
        lc.detail(q)
        q.code()
        time.sleep(1)


if __name__ == "__main__":
    main()
