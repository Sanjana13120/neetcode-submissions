# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        return prev
        

'''
0 1 2 3
       c 

3->2->1->0->None

nxt= none
curr.next= 2
prev= 3
curr= none


'''