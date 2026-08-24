class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:          # O(n logn)
        if self.right and num>self.right[0]:
            heapq.heappush(self.right,num)
        else:
            heapq.heappush(self.left,-num)

        if len(self.left)>len(self.right)+1:
            val=heapq.heappop(self.left)
            heapq.heappush(self.right,-val)

        if len(self.right)>len(self.left)+1:
            val=heapq.heappop(self.right)
            heapq.heappush(self.left,-val)


    def findMedian(self) -> float:             # O(1)
        if len(self.right)>len(self.left):
            return self.right[0]
        elif len(self.left)>len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0])/2.0
        
        

'''
tc: O(nlogn)
sc: O(n)


in this we have to addNum(num) and  findMedian()

addNum(num) -- 

we will have 2 heaps left and right
left will have  [1 2]  
right will have [3 4]

for the median we need left - largest num and right - smallest number
left  - max heap
right - min heap

addNum(1) -- left=[-1] right=[]
addNum(2) -- left=[-2 -1] right=[]
left=[-1] right=[2]
addNum(3) -- left=[-1] right=[2 3]

addNum(4) -- left=[-1] right=[2 3 4]
-- left=[-2 -1] right=[3 4]

addNum(5) -- left=[-2 -1] right=[3 4 5]

findMedian() - return the median of all ele

even length - just return (-left[0]+right[0])/2

odd length - right will have 1 extra num

1

'''