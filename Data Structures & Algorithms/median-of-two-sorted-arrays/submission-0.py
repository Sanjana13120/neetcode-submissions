class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()

        n=len(nums)

        mid  = len(nums)//2

        if n%2==0:
            return (nums[mid]+nums[mid-1])/2
        else:
            return nums[mid]


'''
tc: O((n+m) log(m+n))
sc: O(n+m)
n - len of nums1
m - len of nums2

Input: nums1 = [1,2], nums2 = [3]

goal - find median of two arr

Approach:
1. Combine both arrays.
2. Sort the combined array.
3. Find the middle index.
4. If length is odd:
       return nums[mid]
   Else:
       return (nums[mid] + nums[mid-1]) / 2

-------------------------------------------------------------
Input: nums1 = [1,2], nums2 = [3]

nums = [1 2 3]

n=3
mid=1

3%2==1 so return nums[1]=2

-------------------------------------------------------------
Input: nums1 = [1,3], nums2 = [2,4]

nums= [1 3 2 4]
after sort

nums=[1 2 3 4]

n=4
mid=2

4%2==0? return (nums[2]+nums[1])/2 = (3+2)/2=2.5

'''