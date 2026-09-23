class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for c in range(n):
            dp[0][c]=1

        for r in range(m):
            dp[r][0]=1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


"""
tc: O(m*n)
sc: O(m*n)

Input: m = 3, n = 6

goal - find the number of unique path from (0,0) i have to reach (m-1)(n-1)

so in this from (0,0) to (2,5)

  0 1 2 3 4 5
0 1 1 1 1 1 1
1 1   x
2 1

approach: DP

base:  dp[0][c]=1
       dp[r][0]=1

choice: either down or right 

state: dp[i][j] = no of ways to reach cell (i,j)

transition: say im at (1,2) i can reach (1,2) either from (0,2)down and (1,1)right
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


dp[1][1] = dp[0][1] + dp[1][0] = 1+1=2
dp[1][2] = dp[0][2] + dp[1][1] = 1+2=3
dp[1][3] = dp[0][3] + dp[1][2] = 1+3=4
....
....

dp[2][1] = dp[1][1] + dp[2][0] = 2+1=3

  0 1 2 3 4 5
0 1 1 1 1 1 1
1 1 2 3 4 5 6
2 1 3 6 10 15 21


ans=dp[m-1][n-1]=21

-----------------------------------------------------------------------------------------------------------------------

Input: m = 3, n = 3
  
  0 1 2
0 1 1 1
1 1 2 3
2 1 3 6

ans=6


"""
