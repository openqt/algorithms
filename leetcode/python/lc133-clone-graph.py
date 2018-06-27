# coding=utf-8
import unittest

"""133. Clone Graph
https://leetcode.com/problems/clone-graph/description/

<p>
Clone an undirected graph. Each node in the graph contains a <code>label</code> and a list of its <code>neighbors</code>.
</p>

<div>
<br>
<b>OJ's undirected graph serialization:</b>

<p>
Nodes are labeled uniquely.
</p>

We use <code>#</code> as a separator for each node, and <code>,</code> as a separator for node label and each neighbor of the node.
</p>


<p>
As an example, consider the serialized graph <code><font color="red">{<font color="black">0</font>,1,2#</font><font color="blue"><font color="black">1</font>,2#</font><font color="green"><font color="black">2</font>,2}</font></code>.
</p>

<p>
The graph has a total of three nodes, and therefore contains three parts as separated by <code>#</code>.
<ol>
<li>First node is labeled as <code><font color="black">0</font></code>. Connect node <code><font color="black">0</font></code> to both nodes <code><font color="red">1</font></code> and <code><font color="red">2</font></code>.</li>
<li>Second node is labeled as <code><font color="black">1</font></code>. Connect node <code><font color="black">1</font></code> to node <code><font color="blue">2</font></code>.</li>
<li>Third node is labeled as <code><font color="black">2</font></code>. Connect node <code><font color="black">2</font></code> to node <code><font color="green">2</font></code> (itself), thus forming a self-cycle.</li>
</ol>
</p>

<p>
Visually, the graph looks like the following:
<pre>
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
</pre>
</p>

</div>
Similar Questions:
  Copy List with Random Pointer (copy-list-with-random-pointer)
"""


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
