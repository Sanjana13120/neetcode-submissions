class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n

        dp=[0]*(n+1)

        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
        

'''
tc: O(n)
sc: O(n)

goal - number of distinct ways to climb to the top of the staircase.

dp = [1 1 2 3 5 8 13 ....]

base : n==1 or n==2 return n
state = dp[1]=1 dp[2]=2
transition = dp[i] = dp[i-1] + dp[i-2]

n=2 
1+1
2 

n=3
1+1+1
1+2
2+1

n=4
1+1+1+1
1+1+2
2+1+1
1+2+1
2+2

n=5
1+1+1+1+1
1+1+1+2
1+1+2+1
1+2+1+1
2+1+1+1
1+2+2
2+1+2
2+2+1

n=3
dp=[1 1 2 3]

n=4
dp=[1 1 2 3 5]




'''