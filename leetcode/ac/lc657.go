package main

import (
	"fmt"
)

/*657. Judge Route Circle
https://leetcode.com/problems/judge-route-circle/description/

Initially, there is a Robot at position (0, 0).
Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.

The move sequence is represented by a string.
And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example 1:
	Input: "UD"
	Output: true

Example 2:
	Input: "LL"
	Output: false
*/
func judgeCircle(moves string) bool {
	pos := Cell{0, 0}
	for _, i := range moves {
		switch i {
		case 'R':
			pos.Col++
		case 'L':
			pos.Col--
		case 'U':
			pos.Row--
		case 'D':
			pos.Row++
		}
	}
	return pos == Cell{0, 0}
}

type Cell struct {
	Row, Col int
}

func main() {
	fmt.Println(judgeCircle("UD"))
	fmt.Println(!judgeCircle("LL"))
}
