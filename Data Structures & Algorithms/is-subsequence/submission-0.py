class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


"""
tc: O(n+m)
sc: O(1)

goal-  return true if s is a subsequence of t, or false otherwise.

Input: s = "node", t = "neetcode"


n o d e  
        i

n e e t c o d e
                j

i=0 j=0 n==n? yes so 
i=1 j=1 o==e? no j=2
i=1 j=2 o==e> no j=3
i=1 j=3 o==t? no j=4
i=1 j=4 o==c? no j=5
i=1 j=5 o==o? yes so i+=1 j+=1
i=2 j=6 d==d? yes so i+=1 j+=1
i=3 j=7 e==e? yes so i+=1 j+=1
i=4 j=8

i==len(s) == 4==4? yes return True

----------------------------------------------------------------------------------------
Input: s = "axc", t = "ahbgdc"

a x c
  i

a h b g d c
  j

a==a? i=1 j=1
x==h? no till j=6 x is not equal

i==len(s) ? 1==3?no return False


"""
