class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=nums
        heapq.heapify(self.heap)
        
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)

        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        

'''
tc: O(mlogk)   Where m is the number of calls made to add().
sc: O(k)

["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

kth largest -- min heap

heap = {2 3 3}

add [3] - heap = {3 3 3}
add [5] - heap = {3 3 5}
add [6] - heap = {3 5 6}
add [7] - heap = {5 6 7}
add [8] - heap = {6 7 8}



'''