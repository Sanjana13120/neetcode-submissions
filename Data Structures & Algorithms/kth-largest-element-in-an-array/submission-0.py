class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)

        return nums[0]
        
'''
tc: O(nlogn)
sc: O(1)
Input: nums = [2,3,1,5,4], k = 2

kth largest-- min heap

heap={1 2 3 4 5} k=2

heap={4 5}

'''