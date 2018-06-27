package main

import (
	"fmt"
)

/*576. Out of Boundary Paths
https://leetcode.com/problems/out-of-boundary-paths/description/

<p>There is an <b>m</b> by <b>n</b> grid with a ball. Given the start coordinate <b>(i,j)</b> of the ball, you can move the ball to <b>adjacent</b> cell or cross the grid boundary in four directions (up, down, left, right). However, you can <b>at most</b> move <b>N</b> times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 10<sup>9</sup> + 7.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>m = 2, n = 2, N = 2, i = 0, j = 0
<b>Output:</b> 6
<b>Explanation:</b>
<img src="/static/images/problemset/out_of_boundary_paths_1.png" width = "40%" />
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>m = 1, n = 3, N = 3, i = 0, j = 1
<b>Output:</b> 12
<b>Explanation:</b>
<img src="/static/images/problemset/out_of_boundary_paths_2.png" width = "37%" />
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>Once you move the ball out of boundary, you cannot move it back.</li>
<li>The length and height of the grid is in range [1,50].</li>
<li>N is in range [0,50].</li>
</ol>
</p>
Similar Questions:
  Knight Probability in Chessboard (knight-probability-in-chessboard)
*/
func findPaths(m int, n int, N int, i int, j int) int {
    
}

func main() {
	fmt.Println()
}
