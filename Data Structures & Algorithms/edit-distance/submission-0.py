class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1) + 1
        cols = len(word2) + 1

        dp = [[float("inf")] * (cols) for _ in range(rows)]

        dp[0][0] = 0

        for r in range(1, rows):
            dp[r][0] = dp[r - 1][0] + 1

        for c in range(1, cols):
            dp[0][c] = dp[0][c - 1] + 1

        for r in range(1, rows):
            for c in range(1, cols):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1

        return dp[rows-1][cols-1]


"""
tc: O(rows*cols)
sc: O(rows*cols)


goal - Return the minimum number of operations to make word1 equal word2.

conditions - on word1 i can make 3 opr
        1. delete ch at any position
        2. insert ch at any position
        3. replace ch at any position

Approach: 2D Dynamic Programming

multiple choices- insert, delete, replace

base: dp[0][0] = 0 → Converting an empty string into an empty string requires zero operations.
      dp[i][0] = i → Delete all i characters from word1.
      dp[0][j] = j → Insert all j characters of word2 into an empty string.

state: dp[i][j]= min opr to convert first i ch of word1 into first j ch of word2

transition: When characters don't match: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
            When characters match : dp[i][j] = dp[i-1][j-1]


Input: word1 = "monkeys", word2 = "money"
if we remove k and s word1==word2

rows=7 cols=5

dp[1][1]-- m==m take diagonal
dp[1][2]-- m==mo min(2,0,1)+1=1

      0  1 2 3 4 5
      "" m o n e y
0 ""  0  1 2 3 4 5
1 m   1  0 1 2 3 4
2 o   2  1 0 1 2 3
3 n   3  2 1 0 1 2
4 k   4  3 2 1 1 2
5 e   5  4 3 2 1 2
6 y   6  5 4 3 2 1
7 s   7  6 5 4 3 2


return dp[7][5]=2

--------------------------------------------------------------------------------------------------------------------
Input: word1 = "neatcdee", word2 = "neetcode"

rows=8 cols=8

      0  1 2 3 4 5 6 7 8
      "" n e a t c d e e 
0 ""  0  1 2 3 4 5 6 7 8
1  n  1  0 1 2 3 4 5 6 7
2  e  2  1 0 1 2 3 4 5 6
3  e  3  2 1 1 2 3 4 5 6
4  t  4  3 2 2 1 2 3 4 5
5  c  5  4 3 3 2 1 2 3 4
6  o  6  5 4 4 3 2 2 3 4
7  d  7  6 5 5 4 3 2 3 4
8  e  8  6 6 6 5 4 3 2 3

dp[8][8]=3



"""
