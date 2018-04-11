package main

import (
	"fmt"
)

/* 289. Game of Life
https://leetcode.com/problems/game-of-life/description/

According to the Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

	Any live cell with fewer than two live neighbors dies, as if caused by under-population.
	Any live cell with two or three live neighbors lives on to the next generation.
	Any live cell with more than three live neighbors dies, as if by over-population..
	Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
	Could you solve it in-place? Remember that the board needs to be updated at the same time:
	You cannot update some cells first and then use their updated values to update other cells.

	In this question, we represent the board using a 2D array. In principle, the board is infinite,
	which would cause problems when the active area encroaches the border of the array.
	How would you address these problems?
*/
func gameOfLife(board [][]int) {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			n := lives(board, i, j)
			if board[i][j] == 0 {
				if n == 3 {
					board[i][j] += 10
				}
			} else {
				if n == 2 || n == 3 {
					board[i][j] += 10
				}
			}
		}
	}

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			board[i][j] /= 10
		}
	}
}

func lives(board [][]int, row, col int) (total int) {
	for i := max(0, row-1); i <= min(len(board)-1, row+1); i++ {
		for j := max(0, col-1); j <= min(len(board[0])-1, col+1); j++ {
			total += board[i][j] % 10
		}
	}
	return total - board[row][col]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

const (
	DD = 0 // DEAD->DEAD
	LD = 1 // LIVE->DEAD

	DL = 10 // DEAD->LIVE
	LL = 11 // LIVE->LIVE
)

// https://blog.csdn.net/xudli/article/details/48896549
func main() {
	m := [][]int{
		{1, 1, 0, 1},
		{1, 1, 1, 1},
		{1, 0, 0, 1},
		{0, 0, 0, 1},
	}
	gameOfLife(m)
	for _, i := range m {
		fmt.Println(i)
	}

	m2 := [][]int{
		{1},
		{0},
		{0},
		{1},
		{0},
		{0},
		{1},
		{0},
		{0},
		{1},
	}
	gameOfLife(m2)
}
