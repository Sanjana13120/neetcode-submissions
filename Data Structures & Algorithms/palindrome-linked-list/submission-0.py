# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,curr):
        prev=None

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        return prev


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        if fast:
            slow=slow.next

        rev=self.reverse(slow)

        while rev:
            if head.val != rev.val:
                return False

            head=head.next
            rev=rev.next

        return True
       

'''
tc: O(n)
sc: O(1)
1 2 3 2 1
      s
        f
slow=3
fast=1

fast exists move slow due to odd lenght
slow=2

rev(slow) - 1 2

reverse(2)
curr=2 prev=None

1--2--none

nxt=none
prev=1
curr=none

1 2 3    1 2 
  f        s
until second is e,mpty
1==1 yes
2==2 yes

until rev so true


-----------------------------------------------------------------------

1 2 2 1
    s
         f

slow=2 fast=none

rev(2)-- 1 2

1 2    1 2
  f      s

1==1 yes
2==2 yes





'''