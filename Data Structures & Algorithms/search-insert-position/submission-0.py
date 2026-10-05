class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return start


"""
tc: O(logn)
sc: O(1)
goal - , return the index if the target is found. If not, return the index where it would be if it were inserted in order.

given sorted

approach: binary search

Input: nums = [-1,0,2,4,6,8], target = 5

-1 0 2 4 6 8
       se
       m

start = 0
end = 5
mid = 2
2<5 so start=mid+1

start = 3
end = 5
mid = 4
6>5 so end=mid-1 

start=3
end=3
mid=3
4<5? start=mid+1

start=4 end=3

return start


-------------------------------------------------------

Input: nums = [-1,0,2,4,6,8], target = 10

-1 0 2 4 6 8
           se
           m
start = 0
end = 5
mid = 2
2<5 so start=mid+1

start=3
end=5
mid=4
6<10 start=mid+1

start=5
end=5
mid=5

8<10 start=6 end=5

return start

"""
