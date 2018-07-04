package main

import (
	"fmt"
)

/* 735. Asteroid Collision
https://leetcode.com/problems/asteroid-collision/description/

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Example 1:
	Input:
	asteroids = [5, 10, -5]
	Output: [5, 10]
	Explanation:
	The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:
	Input:
	asteroids = [8, -8]
	Output: []
	Explanation:
	The 8 and -8 collide exploding each other.

Example 3:
	Input:
	asteroids = [10, 2, -5]
	Output: [10]
	Explanation:
	The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4:
	Input:
	asteroids = [-2, -1, 1, 2]
	Output: [-2, -1, 1, 2]
	Explanation:
	The -2 and -1 are moving left, while the 1 and 2 are moving right.
	Asteroids moving the same direction never meet, so no asteroids will meet each other.

Note:
	The length of asteroids will be at most 10000.
	Each asteroid will be a non-zero integer in the range [-1000, 1000]..
*/
func asteroidCollision(asteroids []int) []int {
	var result []int
	for _, i := range asteroids {
		result = collision(result, i)
	}

	return result
}

func collision(asteroids []int, n int) []int {
	if n == 0 {
		return asteroids
	}

	if len(asteroids) == 0 {
		return []int{n}
	}

	pos := len(asteroids) - 1
	if meet(asteroids[pos], n) {
		return collision(asteroids[:pos], absmax(asteroids[pos], n))
	}

	return append(asteroids, n)
}

func meet(a, b int) bool {
	if (a < 0 && b < 0) || (a > 0 && b > 0) || (a < 0 && b > 0) {
		return false
	}
	return true
}

func absmax(a, b int) int {
	aa, bb := a, b
	if a < 0 {
		aa = -a
	}
	if b < 0 {
		bb = -b
	}
	if aa == bb {
		return 0
	}
	if aa > bb {
		return a
	}
	return b
}

func comp(a, b []int) bool {
	//fmt.Println(a, b)
	if len(a) != len(b) {
		return false
	}
	for n, i := range a {
		if i != b[n] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(comp(asteroidCollision([]int{5, 10, -5}), []int{5, 10}))
	fmt.Println(comp(asteroidCollision([]int{8, -8}), []int{}))
	fmt.Println(comp(asteroidCollision([]int{10, 2, -5}), []int{10}))
	fmt.Println(comp(asteroidCollision([]int{-2, -1, 1, 2}), []int{-2, -1, 1, 2}))
}
