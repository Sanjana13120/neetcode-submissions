class Solution:
    def countSubstrings(self, s: str) -> int:

        def palindrome(s,left,right):
            count=0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1

            return count
        total = 0

        for i in range(len(s)):
            odd = palindrome(s,i,i)
            even = palindrome(s,i,i+1)

            total += odd + even

        return total

'''
tc: O(n**2)
sc: O(1)

odd and even length

odd = checkPalidrome(s,i,i)
even = checkPalindrome(s,i,i+1)

0 1 2
a b c

totalcount=0

i=0
odd = (abc,0,0)
a==a? left=-1 right=1 count=1
odd= 1

even = (abc,0,1)
a==b? no count=0
even = 0

total = 1+0= 1

i=1
odd = (abc,1,1)
b==b? yes left=0 right=2 count=1
a==c? no 
odd = 1

even = abc(1,2)
b==c? no count=0 even=0

total = 1+1+0= 2

i=2
odd = (abc,2,2)
c==c? yes left=1 right=3 count=1
3>3? no so odd=1

even= (abc,2,3)
3>3? no even=0

total =2+1+0=3

-------------------------------------------------------------------------------
0 1 2
a a a

i=0
odd = (aaa,0,0)
a==a? yes left=-1 right=1 count=1
odd=1

even = (aaa,0,1)
a==a? yes left=-1 right=2 count=1

total = 0+1+1=2

i=1
odd = (aaa,1,1)
a==a? yes left=0 right=2 count=1
a==a? yes left=-1 right=3 count=2
odd=2

even = (aaa,1,2)
a==a? yes left=0 right=3 count=1
even = 1

total = 2+2+1=5

i=2
odd = (aaa,2,2)
a==2? yes left=1 right=3 count=1
odd =1

even = (aaa,2,3)
3>3? so even=0

total = 5+1+0 = 6


'''