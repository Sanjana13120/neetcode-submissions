class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)

        leftcount = (total + 1) // 2

        start = 0
        end = len(nums1)

        while start <= end:
            cut1 = start + (end - start) // 2
            cut2 = leftcount - cut1

            left1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            left2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]

            right1 = float("inf") if cut1 == len(nums1) else nums1[cut1]
            right2 = float("inf") if cut2 == len(nums2) else nums2[cut2]

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                end = cut1 - 1
            else:
                start = cut1 + 1


"""
Tc: O(log(min(m, n)))
sc: O(1)
goal - find median of two arr


Approach: Binary Search (Optimal)

No need to merge the arrays.

Key Idea:

1. Find a partition such that: 
      max(left) <= min(right)
      left side contains (m+n+1)//2 elements.
2. If total length is even: left_count = right_count
   If total length is odd: left_count = right_count + 1
3. Form the left and right partitions.
4. Once a valid partition is found:

   Even length:  median = (max(left) + min(right)) / 2

   Odd length:  median = max(left)

-------------------------------------------------------------
Input: nums1 = [1,2], nums2 = [3]
total =3
odd length
leftcount = (3+1)/2 = 2

Partition:

nums1 = [1 2 |]
nums2 [ | 3]

left = [1,2]
right = [3]

2<=3 
so median = 2

-------------------------------------------------------------
Input: nums1 = [1,3], nums2 = [2,4]

total = 4
even length
leftcount= (4+1)//2 = 2

Partition:

nums1 = [1 | 3]
nums2 = [2 | 4]

left = [1 2]
right = [3 4]

max(left)<=min(right) = 2<=3

median = (2+3)/2 = 2.5

"""
