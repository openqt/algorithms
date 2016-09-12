'''
Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give? 
'''


class Solution:

    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies.append(candies[i - 1] + 1)
            else:
                candies.append(1)

        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and not (candies[i - 1] > candies[i]):
                candies[i - 1] = candies[i] + 1

        return reduce(lambda x, y: x + y, candies)

if __name__ == '__main__':
    s = Solution()
    assert s.candy([1, 2, 2]) == 4
    assert s.candy([2, 1]) == 3
    assert s.candy([2, 2, 1]) == 4
    print 'PASS'
