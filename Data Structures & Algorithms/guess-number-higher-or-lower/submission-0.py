# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            mid = start + (end - start) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                start = mid + 1
            else:
                end = mid - 1
'''

tc: O(logn)
sc: O(1)

Approach: Binary Search

1. Initialize start = 1 and end = n.
2. Calculate mid = start + (end - start) // 2.
3. Call guess(mid):
- 0: Target found, return mid.
- 1: Guess is too low, search right half (start = mid + 1).
- -1: Guess is too high, search left half (end = mid - 1).
4. Repeat until the target is found.

'''