# coding=utf-8
import unittest

"""71. Simplify Path
https://leetcode.com/problems/simplify-path/description/

<p>Given an absolute path for a file (Unix-style), simplify it.</p>

<p>For example,<br />
<strong>path</strong> = <code>&quot;/home/&quot;</code>, =&gt; <code>&quot;/home&quot;</code><br />
<strong>path</strong> = <code>&quot;/a/./b/../../c/&quot;</code>, =&gt; <code>&quot;/c&quot;</code></p>

<p><strong>Corner Cases:</strong></p>

<ul>
	<li>Did you consider the case where <strong>path</strong> = <code>&quot;/../&quot;</code>?<br />
	In this case, you should return <code>&quot;/&quot;</code>.</li>
	<li>Another corner case is the path might contain multiple slashes <code>&#39;/&#39;</code> together, such as <code>&quot;/home//foo/&quot;</code>.<br />
	In this case, you should ignore redundant slashes and return <code>&quot;/home/foo&quot;</code>.</li>
</ul>

Similar Questions:

"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
