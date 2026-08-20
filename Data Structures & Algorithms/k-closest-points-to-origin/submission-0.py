class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for x,y in points:
            distance=x*x + y*y

            heapq.heappush(heap,(-distance,[x,y]))

            if len(heap)>k:
                heapq.heappop(heap)

        return [points for dist,points in heap]

'''
tc: O(nlogk)
sc: O(k)

kth closest point to (0,0) -- max heap

Input: points = [[0,2],[2,0],[2,2]], k = 2

dist b/2 [0,2] and [0,0] = 4
    heap=[-4,[0,2]]
    
dist b/w [2,0] and [0,0] = 4
    heap=[-4,[0,2], -4,[2,0]]

dist b/w [2,2] and [0,0] = 8
    heap=[-8,[2,2], -4,[0,2], -4,[2,0]]
    if len(heap)>k: 3>2: yes
        heap=[-4,[0,2], -4,[2,0]]

res=[[0,2],[2,0]]




'''