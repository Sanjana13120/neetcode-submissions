class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def backtrack(i, j, k):

            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i<len(s1) and s1[i] == s3[k]:
                if backtrack(i + 1, j, k + 1):
                    return True

            if j<len(s2) and s2[j] == s3[k]:
                if backtrack(i, j + 1, k + 1):
                    return True

            return False

        return backtrack(0, 0, 0)


"""
tc: O(2^ (n1+n2))
sc: O(n1+n2)

n1 - len of s1
n2 - len of s2

goal -  Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.


approach: backtrakcing/recursion

1. start i,k,j=0
2. if s1[i]==s3[k], recurse taking i+1, k+1
3. if s2[j]==s3[k], recurse taking j+1, k+1
4. if k==len(s3) return true

Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

a a a a      
        i

b b b b
        j

a a b b b b a a
                k

backtrack(0,0,0)
    s1[0]==s3[0]? yes 
    backtrack(1,0,1)
        a==a? yes
        backtrack(2,0,2)
            a==b?no
            s2[j]==s3[k]? yes b==b
            backtrack(2,1,3)
                b==b? yes
                backtrack(2,2,4)
                    b==b? 
                    bactrack(2,3,5)
                        b==b?
                        backtrack(2,4,6)
                            a==a? 
                            backtrack(3,4,7)
                                a==a?
                                backtrack(4,4,8)
                                    k==len(s3)= 8==8?yes
                                        return 4==4 and 4==4  -->true


-----------------------------------------------------------------------------------------------------------

Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"

a b c
    i

x y z
  j

a b x z c y
      k

backtrack(0,0,0)
    a==a?
    backtrack(1,0,1)
    b==b? backtrack(2,0,2)
        x==x? backtrack(2,1,3)
            c==z? no 
            y==z? no 
            return False


"""
