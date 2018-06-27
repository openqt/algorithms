# coding=utf-8
import unittest

"""Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/description/

<p>Given a list of airline tickets represented by pairs of departure and arrival airports <code>[from, to]</code>, reconstruct the itinerary in order. All of the tickets belong to a man who departs from <code>JFK</code>. Thus, the itinerary must begin with <code>JFK</code>.</p>

<p><b>Note:</b></p>

<ol>
	<li>If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary <code>[&quot;JFK&quot;, &quot;LGA&quot;]</code> has a smaller lexical order than <code>[&quot;JFK&quot;, &quot;LGB&quot;]</code>.</li>
	<li>All airports are represented by three capital letters (IATA code).</li>
	<li>You may assume all tickets form at least one valid itinerary.</li>
</ol>

<p><b>Example 1:</b></p>

<pre>
<code><strong>Input: </strong>tickets</code> = <code>[[&quot;MUC&quot;, &quot;LHR&quot;], [&quot;JFK&quot;, &quot;MUC&quot;], [&quot;SFO&quot;, &quot;SJC&quot;], [&quot;LHR&quot;, &quot;SFO&quot;]]</code>
<strong>Output: </strong><code>[&quot;JFK&quot;, &quot;MUC&quot;, &quot;LHR&quot;, &quot;SFO&quot;, &quot;SJC&quot;]</code>
</pre>

<p><b>Example 2:</b></p>

<pre>
<code><strong>Input: </strong>tickets</code> = <code>[[&quot;JFK&quot;,&quot;SFO&quot;],[&quot;JFK&quot;,&quot;ATL&quot;],[&quot;SFO&quot;,&quot;ATL&quot;],[&quot;ATL&quot;,&quot;JFK&quot;],[&quot;ATL&quot;,&quot;SFO&quot;]]</code>
<strong>Output: </strong><code>[&quot;JFK&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;SFO&quot;]</code>
<strong>Explanation: </strong>Another possible reconstruction is <code>[&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;ATL&quot;,&quot;SFO&quot;]</code>. But it is larger in lexical order.
</pre>

<p><b>Credits:</b><br />
Special thanks to <a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a> for adding this problem and creating all test cases.</p>

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
