class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[-1] if dp[amount] != amount + 1 else -1


"""
tc: O(amount * len(coins))
sc: O(amount)

goal -  fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

Input: coins = [1,5,10], amount = 12


1+1+10=12

choice: we can take multiple coins

base: it amount==0 return 0

state: dp[i] = minimum number of coins needed to make amount i

transition: for every coin:
                if coin<=i:
                    dp[i]=min(dp[i],1+dp[i-coin])

dp=[0 0 0 0 0 0 0 0 0 0 0 0]

dp[0]=0

dp[1]=1 coin=dp[0]+1=1
dp[2]=1 coins only = dp[2-1]+1=2
dp[3]=dp[3-1]+1=3
dp[4]=dp[4-1]+1=4
dp[5]= take 1 5 coin or 5 1coins
    if i take 1 5coin -- dp[5]=dp[5-5]+1=0+1=1
    if i take 5 1coins -- dp[5]=dp[5-1]+1=5 but we need min coins 
    so dp[5]=1

dp[6]=2
dp[7]= tkae 1 coin dp[6]+1=3 
       take 5 coin dp[2]+1=3

dp[8]= 1coin- dp[7]+1=4
       5coin dp[3]+1=3+1=4

dp[9]= dp[8]+1=5
       dp[4]+1=5

dp[10]= dp[9]+1=6
        dp[5]+1=2
        dp[0]+1=1

dp[11] = dp[10]+1=2
         dp[6]+1=3
         dp[1]+1=2

dp[12]= dp[11]+1=3
        dp[7]+1=4
        dp[2]+1=3

dp=[0 1 2 3 4 1 2 3 4 5 1 2 3]


"""
