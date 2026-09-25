class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0 for _ in range(3)] for _ in range(n)]

        dp[0][0] = 0 - prices[0]
        dp[0][1] = 0
        dp[0][2] = float("-inf")

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2])
            dp[i][2] = dp[i - 1][0] + prices[i]

        return max(dp[n - 1][1], dp[n - 1][2])


"""
tc: O(n)
sc: O(n)

goal - Return the maximum profit you can achieve.

condition - if u sell, we cannot buy one next day and atmost 1 coin at a time

approach: DP - 2D
At each day, I can either buy, sell, or do nothing.

I use 3 states:

1. I am holding a stock.
2. I am not holding a stock and I am not in cooldown.
3. I just sold the stock, so tomorrow is a cooldown day.


base: dp[0][0] = 0 - prices[0]
      dp[0][1] = 0
      dp[0][2] = -inf

state: dp[i][j] = max profit on day i when in state j
    states (j) are
    0 - holding
    1 - not holding and not cooldown
    2 - cooldown

transition: how each state can be reached from yesterday

Case 1: 0 — holding today
Yesterday I was holding → dp[i-1][0]
Yesterday I was not holding → buy today, so profit decreases by prices[i]

dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])

Case 2: 1 — not holding and not in cooldown today
Yesterday I was already not holding and not in cooldown → dp[i-1][1]
Yesterday I was in cooldown → cooldown ends today → dp[i-1][2]

dp[i][1] = max(dp[i-1][1], dp[i-1][2])

Case 3: 2 — cooldown today
To be in cooldown today, I must have sold today.

Yesterday I was holding → dp[i-1][0]
I sell today → profit increases by prices[i]
dp[i][2]= prices[i] + dp[i-1][0]


Input: prices = [1,3,4,0,4]
   0   1   2
0 -1   0  -inf
1 -1   0   2
2 -1   2   3
3  2   3  -1
4  2   3   6

day 1=price=3
dp[1][0] = max(dp[0][0], dp[0][1]-3) = max(-1,-3)=-1
dp[1][1] = max(dp[0][1],dp[0][2]) = max(0,-inf)=0
dp[1][2] = dp[0][0] + 3 = -1+3=2

day 2 = price=4
dp[2][0]=max(-1,-4)=-1
dp[2][1]=max(0,2)=2
dp[2][2]=-1+4=3

day3 -> price=0
dp[3][0]=max(-1,2)=2
dp[3][1]=max(2,3)=3
dp[3][2]=-1+0=-1

day4 -> price=4
dp[4][0]=max(2,-1)=2
dp[4][1]=max(3,-1)=3
dp[4][2]=2+4=6

return dp[4][2]

"""
