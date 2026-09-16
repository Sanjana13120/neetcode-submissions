class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def palindrome(s,left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False

                left+=1
                right-=1
            
            return True

        def backtrack(start):

            if start == len(s):
                res.append(list(path))
                return

            for end in range(start,len(s)):
                if palindrome(s,start,end):
                    path.append(s[start:end+1])

                    backtrack(end+1)

                    path.pop()

        backtrack(0)
        return res

'''
tc: O(n. 2^n)
sc: O(n. 2^n) - including res + recursion
    O(n) - excluding res + recursion

approach: recursion/backtracking

a a b
1. start backtrack(0)
2. if start reached len(s), then we have found one path append to res
3. loop over start to len(s)
    check if its a palidrome add to path
    backtrack(start,end+1)

    then undo/pop

Input: s = "aab"

path = []
res= []

backtrack(0) 
    i=0 
        a is palindrome
        path=[a]
        backtrack(1)
            a is palindrome
            path=[a,a]
            backtrack(2)
                b is palindrome
                path=[a,a,b]
                backtrack(3)
                    3==3? res=[[a,a,b]]
            undo b
            path=[a,a]
        undo a
        path=[a]
    i=1
        s[0:2]=aa is palindrome
        path=[aa]
        backtrack(2)
            s[2:3]=b is palindrom
            path=[aa,b]
            backtrack(3)
                3==3 res=[[a,a,b],[aa,b]]
            undo b
            path=[aa]
        undo aa
    path=[]
    i=2
        s[0:3] ==aab not a palindrome
        return 


'''