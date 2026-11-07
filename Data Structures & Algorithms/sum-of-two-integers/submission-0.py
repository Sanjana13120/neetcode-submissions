class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return a + b

        MASK = 0xFFFFFFFF

        while b != 0:
            xor = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK

            a = xor
            b = carry

        if a > 0x7FFFFFFF:
            return ~(a ^ MASK)

        return a


"""
goal - sum of interger without + opr

Approach: Bit Manipulation

1. XOR (^) → Performs addition without carrying.
2. AND (&) → Identifies positions where both bits are 1.
3. Left shift (<< 1) → Moves carry to the next bit position.
4. Repeat until carry becomes 0.

Python negative integer handling:

1. Python supports arbitrary-precision integers.
2. Use MASK = 0xFFFFFFFF to restrict operations to 32 bits.
3. If result exceeds 0x7FFFFFFF, convert it to signed 32-bit representation using ~(a ^ MASK).

------------------------------------------------------------------------------------------------------

Input: a = 4, b = 7
xor= 4^7= 3
carry = 4&7 <<1 = 4<<1=8

a=3 b=8
xor=3^8=11
carry = 3&8 <<1 =0000

a=11 b=0
return 11



"""
