class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2

            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1

        return nums[start]


"""
tc: O(logn)
sc: O(1)

goal -  return the minimum element of the arr

given arr is rotated sorted arr

approach: binary search
1. start =0 end=len(nums)-1
2. find mid
3. if nums[mid]<nums[end]: minimum is at mid or to the left
        end=mid
    else if nums[mid]>nums[end]: minimum is to the right of mid
        start=mid+1

Input: nums = [3,4,5,6,1,2]

3 4 5 6 1 2
      s e


start = 0  end= 5 mid=2
nums[mid]>nums[end] -- 5>2
so seacrh left side start = 3

start=3 end=5 mid=4
nums[mid]<nums[end] --> 1<4? so it could be min 
end=mid= 4

start=3 end=4 mid=3
6>1 so start=mid+1

start=4 end=4
return nums[start]

-----------------------------------------------------------------------
Input: nums = [4,5,0,1,2,3]

start=0 end=5 mid=2
0<3 so end=mid

start=0 end=2 mid=1
5>0 start=2

start=2 end=2 
return nums[2]=0


"""
