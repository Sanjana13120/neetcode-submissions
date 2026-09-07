class Solution:
    def climbStairs(self, n: int) -> int:
        #optimize approach
        a=1
        b=1

        for _ in range(2,n+1):
            a,b = b,a+b

        return b



'''
tc: O(n)
sc: O(1)

original DP state was:
dp[i] = number of ways to reach stair i

In the optimized version, a and b are simply holding the last two DP states.
a=1 b=1

n=4

a=1 b=2

a=2 b=3

a=3 b=5


'''