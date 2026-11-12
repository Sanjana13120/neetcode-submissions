class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        total = 0
        maxlen = 0

        for right in range(len(nums)):
            total += nums[right]

            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen


"""
tc: O(nlogn)
sc: O(n), Auxiliary Space: O(1)

goal - Return the maximum possible frequency of an element after performing at most k operations.

Approach: Sorting + Sliding Window

1. Sort the array.
2. Expand the window by moving right.
3. Add nums[right] to total.
4. Calculate the operations required to make every element equal to nums[right]: 
    operations = nums[right] * (right - left + 1) - total
5. If operations > k:
   - The current window is invalid.
   - Remove nums[left] from total.
   - Move left forward.
   - Repeat until the window becomes valid.
6. Update maxlen with the current window size:
   maxlen = max(maxlen, right - left + 1)
7. Return maxlen.

Input: nums = [1,2,4], k = 5

0 1 2
1 2 4
    r
l

r = 2 
l = 0
total = 7
maxlen = 3
opr = 4*3-7 > 5?no

return maxlen=3

----------------------------------------------------------------------------------------------------

Input: nums = [1,4,8,13], k = 5

0 1 2 3
1 4 8 13
       r
    l

r = 3
l = 2
total = 21
maxlen = 2
opr = 13*2 - 21


return maxlen=2



"""
