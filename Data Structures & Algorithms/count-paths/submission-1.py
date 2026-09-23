class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]

        return dp[n - 1]


"""
TC: O(m × n)
SC: O(n)

goal - find the number of unique path from (0,0) i have to reach (m-1)(n-1)

Input: m = 3, n = 3
  
  0 1 2
0 1 1 1
1 1 
2 1 

approach: DP 1D

base:  dp = [1] * n
First row has only one way to reach each cell: keep moving right.

choice: either down or right 

state: dp[j] = number of ways to reach the current row's cell at column j

transition: say im at (1,2) i can reach (1,2) either from (0,2)down and (1,1)right
            dp[j] = dp[j-1] + dp[j]

we know dp=[1 1 1]

i=1
next row we can find with help of dp

j=1 -> dp[1]=dp[0]+dp[1]=1+1=2
j=2 -> dp[2]=dp[1]+dp[2]=2+1=3

dp=[1 2 3]

i=2

j=1 -> dp[1]=1+2=3
j=2 -> dp[2]=3+3=6

dp=[1 3 6]

return dp[n-1]

"""
