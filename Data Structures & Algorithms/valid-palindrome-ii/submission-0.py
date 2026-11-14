class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalidrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False

                left+=1
                right-=1
            
            return True
        
        left= 0
        right=len(s)-1

        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return isPalidrome(left,right-1) or isPalidrome(left+1,right)

        return True


'''
tc: O(n)
sC: O(1)

Input: s = "aca"

left=0 right=2 a==a? yes
left=1 right=1 c==c? yes
return True

----------------------------------------------------
Input: s = "abbadc"

0 1 2 3 4 5
a b b a d c

left=0 right=5 a==c? no
    isPalidrome(0,4) 
        left=0 right=4 a!=d F
    isPalidrome(1,5)
        l=1 r=5 b!=d F

-----------------------------------------------------
Input: s = "abbda"
0 1 2 3 4
a b b d a

l=0 r=4 a==a?yes
l=1 r=3 b==d?no
    isPalidrome(1,2)
        l=1 r=2 b==b?yes
        l=2 r=1
        return true
    isPalidrome(2,3)
        l=2 r=3 b!=d return False
    
    T or F=T



'''