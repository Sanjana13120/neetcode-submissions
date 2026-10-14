class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        # tc: O(1)
        # sc: O(1)
        # since 32 bits

        count = 0
        while n:
            count += n & 1
            n >>= 1

        return count


"""
tc: O(logn)
sc: O(1)


goal - Return the number of 1 bits in its binary representation.

Approach: Bit Manipulation

n & 1 checks whether the last bit is 1.
n >>= 1 removes the last bit by shifting right.
Count every 1 encountered.

Input: n = 23
count=0

23&1=10111&00001=00001
count=1
n=23//2=11

11&1=1011&0001=0001
count=2
n=5

101&001=001
count=3
n=2

10&01=00
count=3
n=1

1&1=1
count=4
n=0

return count=4


"""
