class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


"""
tc: O(n)
sc: O(1)

Input: nums = [1,0,1,2]

0 1 1 2
  l h
      m     

num=1 mid=1
num=0 swap low and mid 0 1 1 2 low=1 mid=2
num=1 mid=3
num=2 swap mid and high and high=1
"""
