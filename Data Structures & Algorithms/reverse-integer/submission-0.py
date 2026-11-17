class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = abs(x)
        res = int(str(x)[::-1])

        if org < 0:
            res *= -1
        if res < -2**31 or res > 2**31-1:
            return 0

        return res

'''
tc: O(d)
sc: O(d)

d = Number of digits in x.

Approach: String Manipulation

1. Store the original number to preserve its sign.
2. Convert the number to its absolute value using abs() so we can reverse the digits without worrying about the negative sign.
3. Convert the number into a string and reverse it using [::-1].
4. Convert the reversed string back into an integer.
5. If the original number was negative, multiply the reversed number by -1 to restore its sign.
6. Check whether the reversed number falls within the signed 32-bit integer range:
   - Minimum: -2^31
   - Maximum: 2^31 - 1
7. If the reversed number is outside this range, return 0. Otherwise, return the reversed number.


'''