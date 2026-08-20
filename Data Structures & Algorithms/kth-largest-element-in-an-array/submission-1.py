class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]

        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap,num)
            elif num>heap[0]:
                # heapq.heappop(heap)
                # heapq.heappush(heap,num)
                heapq.heapreplace(heap,num)

        return heap[0]


'''
tc: O(nlogk)
sc: O(k)

min heap

2 3 1 5 4      k=2
n

heap=[]

traverse over the nums
num=2 -- heap=[2]
num=3 -- heap=[2 3]
num=1 -- heap=[2 3]
len(heap)>2 -- pop heap=[2,3]

num=5 -- heap=[2,3,5] len(heap)>2
pop -- heap=[3 5]

num=4 -- heap=[3 4 5] 3>2:
pop --> heap=[4,5]

heap[0]--4






'''