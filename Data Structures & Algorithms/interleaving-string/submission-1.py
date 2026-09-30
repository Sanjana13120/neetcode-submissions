class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:  
        if len(s1)+len(s2) != len(s3):
            return False

        memo = {}

        def dp(i,j):

            if i==len(s1) and j==len(s2):
                return True

            if (i,j) in memo:
                return memo[(i,j)]

            if i<len(s1) and s1[i]==s3[i+j]:
                if dp(i+1,j):
                    memo[(i,j)] = True
                    return True

            if j<len(s2) and s2[j]==s3[i+j]:
                if dp(i,j+1):
                    memo[(i,j)] = True
                    return True
                    
            memo[(i,j)] = False           
                
            return False       

        return dp(0,0)


"""
tc: O(n1*n2)
sc: O(n1*n2) + O(n1+n2)

goal -  Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

Approach: DP + Memoization

base: i == len(s1) and j == len(s2)
        return True

state: dp(i,j) - whether s3 be formed using s1[i:] and s2[j:]

Transition: At state (i, j), the current character in s3 is: s3[i + j]
Since every character consumed from s1 or s2 is also consumed from s3: k = i + j

We have up to two choices:
1. If s1[i] == s3[i + j]:
       try taking the next character from s1
       → dp(i + 1, j)

2. If s2[j] == s3[i + j]:
       try taking the next character from s2
       → dp(i, j + 1)

Either choice can lead to a valid interleaving, so the result is True if either branch succeeds.

Memoization: Different paths can reach the same (i, j) state.
             Store the result of each state in memo so we don't solve the same state repeatedly.

Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

a a a a      
        i

b b b b
        j

a a b b b b a a
                k

memo = {}
backtrack(0,0)
    a==a? yes 
    backtrack(1,0)
        a==a? yes backtrack(2,0)
            b==b? yes backtrack(2,1)
                b==b? backtrack(2,2)
                    b==b? yes backtrack(2,3)
                        b==b? yes backtrack(2,4)
                            a==a? yes backtrack(3,4)
                                a==a?backtrack(4,4)
                                    4==4 and 4==4? so memo ={(4,4): True}
                                return memo ={(4,4): True, (3:4):True}
                        memo = {(4,4): True,(3,4): True,(2,4): True}


finally memo = {(4,4): True, (3,4): True,(2,4): True, (2,3): True, (2,2): True, (2,1): True, (2,0): True, (1,0): True, (0,0): True}

     



"""
