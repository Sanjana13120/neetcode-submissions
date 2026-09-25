class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prevhold = -prices[0]
        prevfree = 0
        prevcooldown = float("-inf")

        for price in prices[1:]:
            currhold = max(prevhold, prevfree - price)
            currfree = max(prevfree, prevcooldown)
            currcooldown = prevhold + price

            prevhold = currhold
            prevfree = currfree
            prevcooldown = currcooldown

        return max(prevfree, prevcooldown)


"""
tc: O(n)
sc: O(1)

goal - Return the maximum profit you can achieve.

condition - if u sell, we cannot buy one next day and atmost 1 coin at a time

approach: DP - 1d space optimized 
At each day, I can either buy, sell, or do nothing.

I use 3 states:

1. I am holding a stock.
2. I am not holding a stock and I am not in cooldown.
3. I just sold the stock, so tomorrow is a cooldown day.


base:   prevhold = -prices[0]
        prevfree = 0
        prevcooldown = -inf

state: dp[i][j] = max profit on day i when in state j
    states (j) are
    0 - holding
    1 - not holding and not cooldown
    2 - cooldown

transition:
Notice that every state on day i only depends on the previous day's states:

dp[i][0] - dp[i-1][0], dp[i-1][1] - prices[i]
dp[i][1] - dp[i-1][1], dp[i-1][2]
dp[i][2] - dp[i-1][0] + prices[i]

Therefore, I don't need the entire 2D DP table.

I only need: prevhold, prevfree and prevcooldown

currhold = max(prevhold, prevfree - prices[i])
currfree = max(prevfree, prevcooldown)
currcooldown = prevhold + prices[i]

After calculating all three current states:

prevhold = currhold
prevfree = currfree
prevcooldown = currcooldown

This is important because all three current states must be calculated using the old previous values.

Input: prices = [1,3,4,0,4]

prevhold = -1
prevfree = 0
prevcooldown = -inf

day 1
currhold = max(-1,-3)=-1
currfree = max(0,-inf)=0
currcool = -1+3=2



"""
