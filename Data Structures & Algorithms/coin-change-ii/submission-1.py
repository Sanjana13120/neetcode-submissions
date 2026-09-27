class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]


"""
tc: O(amount * len(coins))
sc: O(amount)


goal  - Return the number of distinct combinations that total up to amount otherwise 0

Input: coins = [1,5,10], amount = 12

10+1+1
5+5+1+1
1+1+1+1+1+1+1+1+1+1+1+1
5+1+1+1+1+1+1+1

so 4 ways

approch: dp

base: no of ways to make amount 0 is 1 dp[0]=1

state: dp[i] = no of ways to make the amount i

transition: dp[i] += dp[i-coin]

Loop order
for coin in coins:
    for i in range(coin, amount + 1):

Why coin first? Because order doesn't matter:
1 + 2 = 2 + 1
We want to count that once, not twice.

Input: amount = 4, coins = [1,2,3]

dp=[1 0 0 0 0]

dp[1]- how many ways i can make amount 1 
with coin 1-- 1 way

dp[2]= with coin 1 1+1 and coin 2 2 so total 2 ways

dp[3]- with coin1- 1+1+1
            coin2- 1+2
            coin3- 3
        3 ways

dp[4]- with coin1- 1+1+1+1
            coin2- 1+1+2 or 2+2
            coin3- 1+3=1
        so 4ways?

dp=[1 0 0 0 0]

coin 1
    i=1 dp[1]+=dp[0]=1
    i=2 dp[2]+=dp[1]=1
    i=3 dp[3]+=dp[2]=1
    i=4 dp[4]+=dp[3]=1

1
1+1
1+1+1
1+1+1+1


dp=[1 1 1 1 1]

coin 2
    i=1 2<=1? no
    i=2 dp[2]+=dp[0]=1+1=2
    i=3 dp[3]+=dp[1]=1+1=2
    i=4 dp[4]+=dp[2]=1+2=3

1+1+1+1
1+1+2
2+2

dp=[1 1 2 2 3]

coin 3
    i=1 3<=1? no
    i=2 3<=2? no
    i=3 dp[3]+=dp[0]=2+1=3
    i=4 dp[4]+=dp[1]=3+1=4 

dp=[1 1 2 3 4]

------------------------------------------------------------------------------------------------------

Input: amount = 7, coins = [2,4]

dp=[1 0 0 0 0 0 0 0]

coin 2:
    i=2 dp[2]+=dp[0]=1
    i=3 dp[3]+=dp[1]=0
    i=4 dp[4]+=dp[2]=1
    i=5 dp[5]+=dp[3]=0
    i=6 dp[6]+=dp[4]=1
    i=7 dp[7]=0

dp=[1 0 1 0 1 0 1 0]

coin 4
    i=4 dp[4]+=dp[0]=2
    i=5 dp[5]+=dp[1]=0
    i=6 dp[6]+=dp[2]=2
    i=7 dp[7]+=dp[3]=0


dp=[1 0 1 0 2 0 2 0]

dp[7]=0


"""
