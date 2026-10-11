class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1 or n==7:
            return True

        if n < 10:
            return False

        total = 0

        while n != 0:
            r = n % 10
            total += r * r
            n //= 10

        return self.isHappy(total)


'''
tc: O(logn)
sc: O(k)


goal -  return true if it is a non-cyclical number, otherwise return false.

non-cyclical number --> sum of square of digits == 1 

Approach: Recursion
1. Base case: If n == 1, return True because the number is happy.
2. If n < 10 and n != 1, return False because no other single-digit number reaches 1 through repeated digit-square transformations.
3. Calculate the sum of the squares of the digits using % 10 and // 10.
4.  Recursively call isHappy(total) until a base case is reached.

'''