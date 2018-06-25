import json
import logging
import requests
import sys
import prettytable

logging.basicConfig(level=logging.DEBUG)


class Question(object):
    def __init__(self, **kwargs):
        stat = kwargs.get("stat")
        if stat:
            self.qid = stat.get("frontend_question_id")
            self.title = stat.get("question__title")
            self.slug = stat.get("question__title_slug")

        self.paid = kwargs.get("paid_only", False)

        difficulty = kwargs.get("difficulty")
        self.level = difficulty.get("level", 0)


class LC(object):
    def __init__(self):
        self.url = "https://leetcode.com/api/problems/algorithms/"
        self.sess = requests.session()
        self.vals = []

    def list(self):
        resp = self.sess.get(self.url)
        resp.raise_for_status()

        data = resp.json()
        logging.info(data.get("category_slug"))
        logging.info("num_total {}".format(data.get("num_total")))

        for status in data["stat_status_pairs"]:
            self.vals.append(Question(**status))

    def show(self):
        pt = prettytable.PrettyTable(["ID", "Title", "Level", "Paid"])
        pt.align["Title"] = "l"
        for i in self.vals:
            pt.add_row([i.qid, i.title, i.level, "X" if i.paid else " "])
        print(pt)
        print("Total: {}".format(len(self.vals)))

    def problem(self, slug):
        data = self.__getQuestionDetail(slug)
        json.dump(data, sys.stdout, indent=2)

        question = data["question"]
        code = json.loads(question["codeDefinition"])
        json.dump(code, sys.stdout, indent=2)
        print(code[2]["defaultCode"])

    def __getQuestionDetail(self, slug):
        url = "https://leetcode.com/problems/{}/description/".format(slug)
        if not self.sess.cookies.get("csrftoken"):
            self.sess.get(url)

        q = {
            "operationName": "getQuestionDetail",
            "variables": {"titleSlug": slug},
            "query": """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    questionTitle
    questionTitleSlug
    content
    difficulty
    stats
    similarQuestions
    categoryTitle
    codeDefinition
    sampleTestCase
    metaData
    envInfo
    article
    topicTags {
      name
      slug
      translatedName
      __typename
    }
    __typename
  }
  isPremium
}""",
        }
        self.sess.headers["referer"] = url
        self.sess.headers["x-csrftoken"] = self.sess.cookies["csrftoken"]
        resp = self.sess.post("https://leetcode.com/graphql", json=q)
        resp.raise_for_status()
        return resp.json().get("data")


def main():
    lc = LC()
    # lc.list()
    # lc.show()
    lc.problem("two-sum")


if __name__ == "__main__":
    main()
