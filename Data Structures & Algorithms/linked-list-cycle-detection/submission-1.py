# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True

        return False
        

'''
tc: O(n)
sc: O(1)
1->2->3->4->2->3->4->2->3->4->2->3->4
         s
                  f

1->2->3
   s
      f

1->2
s
f

'''