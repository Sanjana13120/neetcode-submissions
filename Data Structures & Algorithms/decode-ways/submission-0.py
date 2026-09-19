class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            if "1" <= s[i - 1] <= "9":
                dp[i] += dp[i - 1]

            if i>=2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]


"""
tc: O(n)
sc: O(n)

given - string consisting of uppercase english characters can be encoded to a number 1-26 with A-Z resp

there should not be leading zero

goal:  return the number of ways to decode it.

s = "12"

either (1 2) or 12 -- AB or L

s=226

2 2 6 = BBF
22 6  =  VF
2 26  = BZ

3 ways

Approach:

At every position, look at the end of the current prefix.

There are at most two possibilities:

Take the last one digit.
Take the last two digits.

base: dp[0]=1   

state:dp[i] = ways to decode the first i characters.

transition: For every i, consider the last digit.

1. One-digit choice

If: s[i-1] ∈ "1"..."9" then the digit can stand alone.

Every decoding of the previous prefix can be extended with this digit: dp[i] += dp[i-1]

Think: previous prefix | current digit

2. Two-digit choice

Take: s[i-2:i]

Convert it to a number.

If it is between: 10 and 26, then it is a valid letter.

Every decoding of the prefix before those two digits can be extended with this pair: dp[i] += dp[i-2]

dp=[0 0 0 0]

dp[1]=1
dp[2]=22 can be spilt 2 | 22 - 2 ways
dp[3]= 6 can be split 22 6 or 2 26 or 2 2 6-- 3 ways 

dp=[0 1 2 3]

dp[i]= dp[i-1] + dp[i-2]


"""
