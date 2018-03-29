package main

import (
	"fmt"
	"sort"
)

/*322. Coin Change
https://leetcode.com/problems/coin-change/description/

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
	coins = [1, 2, 5], amount = 11
	return 3 (11 = 5 + 5 + 1)

Example 2:
	coins = [2], amount = 3
	return -1.

Note:
	You may assume that you have an infinite number of each kind of coin.
*/
func coinChange(coins []int, amount int) int {
	book := make([]Cell, amount+1)
	sort.Sort(sort.Reverse(sort.IntSlice(coins)))

	for row := 0; row < len(coins); row++ {
		for col := coins[row]; col <= amount; col++ {
			cur := book[col]
			pre := book[col-coins[row]]
			if cur.Amount < (coins[row] + pre.Amount) {
				book[col] = Cell{coins[row] + pre.Amount, pre.Num + 1}
			} else if cur.Amount == (coins[row] + pre.Amount) {
				if pre.Num+1 < cur.Num {
					book[col].Num = pre.Num + 1
				}
			}
		}
	}

	//fmt.Println(book)
	if book[amount].Amount == amount {
		return book[amount].Num
	}
	return -1
}

type Cell struct {
	Amount, Num int
}

func main() {
	fmt.Println(coinChange([]int{1, 2, 5}, 11) == 3)
	fmt.Println(coinChange([]int{2}, 3) == -1)
	fmt.Println(coinChange([]int{2, 5, 10, 1}, 27) == 4)
	fmt.Println(coinChange([]int{186,419,83,408}, 6249) == 20)
}
