# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,curr):
        prev=None

        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None:
            return 

        slow=fast=head
        prev=None

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None

        second=self.reverse(second)
        first=head

        while first and second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2
                   
        

'''
tc: O(n)
sc: O(1)

2 4 6 8
    s
        f

slow=6
fast=none

second= 8 and slow.next=none

2-4-6-none and 8-none

first=4
second=none

temp1=4-6-none
temp2=none

2-8-4-6-none
-------------------------

2 4 6 8 10
    s
         f

slow=6 fast=10
second=8-10-none


2-4-6-none   and 8-10-none

after rev

2-4-6-none and 10-8-none

first=4
second=8

temp1=6
temp2=none

2-10-4-8-6



'''