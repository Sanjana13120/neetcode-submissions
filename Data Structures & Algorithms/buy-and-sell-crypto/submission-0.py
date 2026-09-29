class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        profit = 0

        for num in prices:
            cost = min(cost, num)
            profit = max(profit, num - cost)

        return profit


"""
tc: O(n)
sc: O(1)

goal - Return the maximum profit else 0

Input: prices = [10,1,5,6,7,1]

10 1 5 6 7 1
           i

cost = min(cost, prices[i])
profit = max(profit, prices[i]-cost)

cost = 1
profit = 6

Input: prices = [10,8,7,5,2]

10 8 7 5 2
         i

cost = 2
profit = 0


"""
