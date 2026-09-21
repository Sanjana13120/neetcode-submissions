class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet =  set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)

        maxLen= max(map(len,wordSet))

        dp[0] = True

        for i in range(n + 1):
            for j in range(max(0,i-maxLen),i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True

        return dp[n]


"""
tc: O(n * L^2)
sc: O(n)

L is the maximum dictionary-word length.

goal - return true if s can be segmented into a space-separated sequence of dictionary words.

approach: DP

base: dp[0] = T

state: dp[i] = true if s[:i] can be segmented into dictionary words

Transition:
For each i, try every valid split point j.

If:   dp[j] == True AND s[j:i] ∈ wordSet
then: dp[i] = True

=============================================================================================================================
Optimization:

For each i, we need a split point j such that:

length of s[j:i] <= maxLen

i - j <= maxLen

Therefore: j >= i - maxLen

So instead of checking:
j = 0 ... i-1

we only check:
j = max(0, i-maxLen) ... i-1

=============================================================================================================================

Input: s = "neetcode", wordDict = ["neet","code"]

0 1 2 3 4 5 6 7
n e e t c o d e

dp=[T F F F T F F F T]

dp[1] --> n ==neet or n==code? no
dp[2] --> ne ==neet or ne==code? no
dp[3] --> nee ==neet or nee==code? no
dp[4] --> neet ==neet or neet==code? yes so  True
dp[5] --> s[4:5]
dp[6] --> s[4:6]
dp[7] --> s[4:7]
dp[8] --> s[4:8] in wordDict? yes 
dp[8] = T

return dp[n]

-----------------------------------------------------------------------------------------------------------------------
s = "applepenapple"
wordDict = ["apple", "pen"]

0 1 2 3 4 5 6 7 8 9 10 11 12
a p p l e p e n a p  p  l e

dp= [T F F F F T F F T F F F F T]

dp[1] --> a in WordDict? no
dp[2] --> ap in WordDict? no
dp[3] --> app in WordDict? no
dp[4] --> appl in WordDict? no
dp[5] --> apple in WordDict? yes =true
dp[6] --> s[5:6] p in WordDict? no
dp[7] --> s[5:7] pe in WordDict? no
dp[8] --> s[5:8] pen in WordDict? yes t
dp[9] --> s[8:9] a in WordDict? no
dp[10] --> s[8:10] ap
dp[11] --> s[8:11] app
dp[12] --> s[8:12] appl
dp[13] --> s[8:13] apple ? yes T
 
-----------------------------------------------------------------------------------------------------------------------
Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]




"""
