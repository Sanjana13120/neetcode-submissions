class Solution:
    def longestPalindrome(self, s: str) -> str:
        largest = ""
        def isPalindrome(s,left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]


        for i in range(len(s)):
            odd = isPalindrome(s,i,i)
            if len(odd) > len(largest):
                largest = odd


            even = isPalindrome(s,i,i+1)
            if len(even) > len(largest):
                largest = even

        return largest
        

'''
bruteforce:
    genetate all possible palindrome stings
    and keep checking if palidrome or not

tc: O(n**3)
sc: O(n)

2 pointers: Expand around center approach
tc : O(n**2)
sc: O(1) 
    O(n) for output string

    run palidrome func for odd and even
    odd = isPalindrome(s,i,i)
    even = isPalindrome(s,i,i+1)
0 1 2 3 4
a b a b d -- odd lenght
i
largest= ""

i=0
odd = (ababd,0,0)
a==a? left-=1 right+=1 
left=-1 right=1
odd = a

largest = a

even = (ababd,0,1)
a==b? no
even=""

i=1
odd = (ababd,1,1)
b==b? yes left=0 right=2
a==a? yes left=-1 right=3
odd = s[0:3] = aba

largest= aba
even= (ababd,1,2)
b==a? no
even=s[2:2]=""

-------------------------------------------------------------------------------
0 1 2 3
a b b c

i=0
odd = (abbc,0,0)
0==0? yes  left=-1 right=1
odd = s[0:1] =a
largest=a

even = (abbc,0,1)
a==b? no
even = s[1:1] =""

i=1
odd = (abbc, 1,1)
b==b? yes left=0 right=2
a==b? no 
odd = s[1:2] = b

even = (abbc,1,2)
b==b? yes left=0 right=3
a==c? no
even = s[1:3] == bb

len(even)> len(largest)? 2>1? yes
largest = bb

i=2
odd = (abbc,2,2)
c==c? yes left=1 right=3>4? no
odd=s[2:3]=c

even = (abbc,2,3)
b==c? no
even = s[3,3]=""

return bb
'''