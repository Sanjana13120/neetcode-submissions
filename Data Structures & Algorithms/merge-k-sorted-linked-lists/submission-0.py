# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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


'''
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



'''