class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bit = n & 1
            ans = (ans<<1) | bit
            n=n>>1
        
        return ans


"""
tc: O(1)
sc: O(1)

goal - Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Input: n = 00000000000000000000000000010101

10101=21

i=0
    bit=1
    ans=1
    n=10

i=1
    bit=0
    ans=10
    n=5

i=2
    bit=1
    ans=101
    n=2

i=3
    bit=0
    ans=101<<1 = 1010 | 0 = 1010
    n=1

i=4
    bit=1
    ans=1010<<1|1 = 10100 |1 =10101
    n=0




"""
