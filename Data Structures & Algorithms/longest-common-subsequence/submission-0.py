class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


"""
tc: O(m*n)
sc: O(m*n)

m-len of text1
n-len of text2

goal- length of the longest common subsequence between the two strings if one exists, otherwise return 0.

cat and crabt

"What is the longest subsequence that both strings can form?"

0 1 2 3 4
c r a b t

0 1 2
c a t


approch: thinking of dp since we have to find the no of length of chars

base: If i reaches the end of text1 OR j reaches the end of text2, there are no characters left to match, so answer = 0.
        if i==len(text1) or j==len(text2)
            answer=0
    so basically
        dp[len(text1)][j] = 0
        dp[i][len(text2)] = 0

state: dp[i][j] = LCS length between text1[i:] and text2[j:]

transition: if text1[i]==text2[j] (if chars match):
                dp[i][j] = 1+dp[i+1][j+1]
            if text1[i]!=text2[j] (if char not match):
                dp[i][j]= max(skip text1, skip text2)
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

c == c len=1

so now at and rabt  ie text1[1:] and text2[2:]
r!=a
so either skip r or skip a
if i skip r then at vs abt a==a so len=2 ca

now t vs bt
t!=b
skip t "" vs bt?no
skip b t vs t t==t so len=3 cat

    0 1 2 3 4 5
    c r a b t "
0 c 3 2 2 1 1 0
1 a 2 2 2 1 1 0
2 t 1 1 1 1 1 0
3 " 0 0 0 0 0 0

len(text1)=3
len(text2)=5

we know i=3 and j=5 is empty

loop i from 2,1,0
loop j from 4,3,2,1,0

i=2 j=4
text1[2]== text2[4] =t
dp[2][4] = 1+ dp[3][5]=1

i=2 j=3 t!=b
dp[2][3]=max(dp[3][3], dp[2][4])=max(0,1)=1

i=2 j=2 t!=a
dp[2][2]=max(0,1)=1

i=2 j=1 t!=r
dp[2][1]=max(0,1)=1

i=2 j=0 t!=c
dp[2][0]=1

i=1 j=4 a!=t dp[1][4]=1
i=1 j=3 a!=b dp[1][3]=1
i=1 j=2 a==a dp[1][2]=2
i=1 j=1 a!=r dp[1][1]=2
i=1 j=0 a!=c dp[1][0]=2

i=0 j=4 c!=t dp[0][4]=1
i=0 j=3 c!=b dp[0][3]=1
i=0 j=2 c!=a dp[0][2]=2
i=0 j=1 c!=r dp[0][1]=2
i=0 j=0 c==c dp[0][0]=3

return dp[0][0]=3


----------------------------------------------------------------------------

"""
