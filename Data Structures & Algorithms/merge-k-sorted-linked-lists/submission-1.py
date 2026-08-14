# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def merge(self,l1,l2):
        dummy=ListNode(0)
        curr=dummy

        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next

            else:
                curr.next=l2
                l2=l2.next

            curr=curr.next

        curr.next=l1 or l2

        return dummy.next   

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #divide and conquer approach
        if not lists:
            return None

        interval=1

        while interval<len(lists):
            for i in range(0,len(lists)-interval,interval*2):
                lists[i]=self.merge(lists[i],lists[i+interval])

            interval*=2  

        return lists[0]     


'''
tc: O(nlogk)
sc: O(1)

l1= [1 2 4]  l2= [1 3 5]  l3= [3 6]

l1 l2 l3

l1+l2  l3

l1+l2+l3

l1 l2 l3 l4

l1+l2  l3+l4

interval=1,2,4,8,16,...

len(lists)=3

1<3 
    i in range(0,2,2)
        list[0]=list[0]+list[1]

[1 1 2 3 4 5]  [1 3 5] [3 6]

interval=1*2=2
2<3
    i in range(0,1,4)
        list[0]=list[0]+list[2]

[1 1 2 3 3 4 5 6] [1 3 5] [3 6]

interval=4
4<3 false 

we return list[0]


merge l1 and l2
[1 2 4]  [1 3 5]

dummy - 1
        curr

'''

""" 
        dummy=ListNode(0)
        curr=dummy

        heap=[]

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))

        
        while heap:
            val,i,node=heapq.heappop(heap)
            curr.next=node
            curr=curr.next

            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))

        return dummy.next    


tc: O(nlogk)
sc: O(k)

Input: lists = [[1,2,4],[1,3,5],[3,6]]
l1= [1 2 4]
l2= [1 3 5]
l3= [3 6]

heap = []

dummy - 1 -1 -2 -3- 3 -4- 5- 6
                             curr

val   = 6
i     = 3
node  = 6

"""