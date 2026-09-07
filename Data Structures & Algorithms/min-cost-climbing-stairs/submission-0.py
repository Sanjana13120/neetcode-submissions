class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp = [0]*(n+1)
        
        dp[0] = 0
        dp[1] = 0

        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[n]

'''
tc: O(n)
sc: O(n)
Goal - Return the minimum cost to reach the top of the staircase

n = len(cost)
dp=[0 0 0 0]

State: dp[i] = minimum cost required to reach position i

Base: dp[0] = 0 and dp[1] = 0

transition:  dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

cost = [1 2 3]
dp=[0 0 0 0]
0-> 2
1->2
dp[2] = min(dp[1]+cost[1], dp[0]+cost[0])
      = min(2,1)=1

dp=[0 0 1 0]

2->3
1->3
dp[3] = min(dp[2]+cost[2], dp[1]+cost[1])
      = min(4, 2)=2

dp=[0 0 1 2]

return dp[n]
------------------------------------------------------------------------------------------------------
Input: cost = [1,2,1,2,1,1,1]

dp = [0 0 0 0 0 0 0 0]

dp[2] 
0->2 or 1->2
= min(1,2)=1

dp = [0 0 1 2 0 0 0 0]

dp[3] --> 2-3 or 1-3
min(2,2)=2

dp[4] --> 2-4 or 3-4
min(2,4)=2

dp = [0 0 1 2 2 0 0 0]

dp[5] --> 3-5 or 4-5
min(4,3)=3

dp = [0 0 1 2 2 3 0 0]

dp[6] --> 4-6 or 5-6
min(3, 4)=3

dp = [0 0 1 2 2 3 3 0]

dp[7] --> 5-7 or 6-7
min(4, 4)=4

dp = [0 0 1 2 2 3 3 4]

dp[n]=4





'''