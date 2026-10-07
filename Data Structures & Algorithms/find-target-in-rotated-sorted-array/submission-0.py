class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = start + (end-start)//2

            if nums[mid]==target:
                return mid

            elif nums[start]<=nums[mid]:
                if nums[start]<=target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1

        return -1


'''
tc: O(logn)
sc: O(1)

goal -  find the index of the target

arr is sorted and rotated

approach: binary search

1. start=0 end=len(nums)-1 and find mid
2. if nums[mid]==target: return mid
3. if nums[start]<=nums[mid] 
        left half is sorted
        if nums[start]<=target<nums[mid]:
            end=mid-1
        else 
            start=mid+1
    else Right half is sorted.
        if nums[mid]<target<=nums[end]:
            start=mid+1
        else:
            end=mid-1




Input: nums = [3,4,5,6,1,2], target = 1

0 1 2 3 4 5
3 4 5 6 1 2
      sme

start=0 end=5 mid=2

3<5 and target lies between 3 and 5? 3<=1<5 no
    start = mid+1 = 3

start=3 end=5 mid=4
nums[mid]==target? 1==1 return mid=4

-----------------------------------------------------------------

Input: nums = [3,5,6,0,1,2], target = 4

0 1 2 3 4 5
3 5 6 0 1 2
  se

start=0 end=5 mid=2
3<6? yes and 3<=4<6? yes end=mid-1

start=0 end=1 mid=0
3<=3? 3<=4<3? no start=mid+1

start=1 end=1 mid=1
5<=5? yes 5<=4<5?no 

start=2 end=1

return -1


'''