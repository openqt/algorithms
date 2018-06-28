# coding=utf-8
import unittest

"""332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/description/

Given a list of airline tickets represented by pairs of departure and arrival
airports `[from, to]`, reconstruct the itinerary in order. All of the tickets
belong to a man who departs from `JFK`. Thus, the itinerary must begin with
`JFK`.

**Note:**

  1. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.
  2. All airports are represented by three capital letters (IATA code).
  3. You may assume all tickets form at least one valid itinerary.

**Example 1:**

    
    
    **Input:** tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    **Output:**["JFK", "MUC", "LHR", "SFO", "SJC"]
    

**Example 2:**

    
    
    **Input:** tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    **Output:**["JFK","ATL","JFK","SFO","ATL","SFO"]
    **Explanation:** Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
    

**Credits:**  
Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi)
for adding this problem and creating all test cases.


Similar Questions:

"""


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
