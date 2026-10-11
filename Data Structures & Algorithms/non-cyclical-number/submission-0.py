class Solution:

    
    def isHappy(self, n: int) -> bool:

        def sumofsquares(n):
            total = 0

            while n != 0:
                r = n % 10
                total += r * r
                n //= 10

            return total

        slow = n
        fast = sumofsquares(n)

        while fast!=1 and slow!=fast:
            slow = sumofsquares(slow)
            fast = sumofsquares(sumofsquares(fast))

        return fast==1

"""
tc: O(logn)
sc: O(1)

goal -  return true if it is a non-cyclical number, otherwise return false.

non-cyclical number --> sum of square of digits == 1 

Approach — Floyd's Cycle Detection Algorithm
1. Create a helper function sumofsquares(n) to calculate the sum of the squares of the digits.
2. Initialize two pointers:
    slow = n
    fast = sumofsquares(n)
3. Move slow one step at a time and fast two steps at a time using the helper function.
4. Continue until fast == 1 or slow == fast.
5. If fast == 1, return True because the number is happy.
6. Otherwise, a cycle has been detected that does not reach 1, so return False.

Key idea: Use two pointers moving at different speeds to detect a cycle without storing previously visited numbers.


Input: n = 100

sum of square of digits = 1+0+0=1

return True

------------------------------------------------------------------------------------------------------------

"""
