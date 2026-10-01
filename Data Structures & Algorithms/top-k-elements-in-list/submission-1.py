class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap)>k:
                heapq.heappop(heap)

        return [num for count, num in heap]


"""
tc: O(nlogk)
sc: O(n)

goal - return top k most freq elements

Input: nums = [1,2,2,3,3,3], k = 2

1:1 2:2 3:3
k>=2? is 2 and 3

res= [2,3]

approch 2: heap

1. if heap has few k ele -- add to heap
2. if heap has k ele then compare the count and replace with large freq

heap = [(2,2),(3,3)]




"""