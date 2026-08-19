class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)

            if x<y:
                heapq.heappush(stones,x-y)
        
        return abs(stones[0]) if stones else 0


        

'''
tc: O(nlogn)
sc: O(n)
Input: stones = [2,3,6,2,4]
we need heaviest stone so max heap

heap = {-6 -4 -3 -2 -2}

x=-6 y=-4 --> -6<-4? yes soo append -6+4=-2 to heap
heap = {-3 -2 -2 -2}

x=-3 y=-2 -3<-2? yes so append -3+2=-1 to heap
heap={-2 -2 -1}

x=-2 y=-2 x==y ---both stones destroyed
heap={-1}



'''