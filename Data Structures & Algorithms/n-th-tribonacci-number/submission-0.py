class Solution:
    def tribonacci(self, n: int) -> int:
        # dp=[0]*(n+1)
        # if n<=2:
        #     return 1 if n!=0 else 0

        # dp[0]=0
        # dp[1]=1
        # dp[2]=1

        # for i in range(3,n+1):
        #     dp[i]= dp[i-3]+dp[i-2]+dp[i-1]

        # return dp[n]

        # space optimized
        # tc: O(n)
        # sc: O(1)

        if n<=2:
            return 1 if n!=0 else 0

        a,b,c=0,1,1

        for _ in range(3,n+1):
            a,b,c=b,c,a+b+c

        return c

        
'''
DP array:
tc: O(n)
sc: O(n)
base:dp[0]=0 dp[1]=1 dp[2]=1

state: dp[i] = tn

transition: dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
0,1,1,2,4,7,13

dp=[0 1 1 0 0 0 0]

dp[3]=dp[0]+dp[1]+dp[2]
      dp[i-3]+dp[i-2]+dp[i-1]



'''