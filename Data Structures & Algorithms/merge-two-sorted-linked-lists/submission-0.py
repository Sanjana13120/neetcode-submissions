# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=tail=ListNode(0)
        
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next

            tail=tail.next

        tail.next=list1 or list2

        return dummy.next
        
'''
tc: O(n+m)
sc: O(1)
l1= [1 2 4]
l2= [1 3 5]

l1= []
l2= [5]

dummy->1->1->2->3->4->5
h
                    t


'''