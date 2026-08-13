# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy=ListNode(0)
        dummy.next=head

        slow=fast=dummy

        for _ in range(n+1):
            fast=fast.next

        while fast:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next

        return dummy.next
        

'''
tc: O(n)
sc: O(1)

5  n=1
dummy-5
s
         f 

dummy.next=none
dummy-none --> []

-----------------------------------

1 2 3 4    n=2

dummy-1-2-3-4
s
          f

slow=dummy
fast=3

dummy-1-2-3-4
   s      f

slow=1
fast=4

dummy-1-2-3-4
      s     f

slow=2
fast=none

dummy-1-2-3-4
        s     f

2.next=4

dummy-1-2-4            
----------------------------
1 2 n=2

dummy-1-2
s
            f

'''