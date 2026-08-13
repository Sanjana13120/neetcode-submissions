# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0

        dummy=ListNode(0)
        curr=dummy

        while l1 or l2 or carry!=0:
            total=carry
            if l1:
                total+=l1.val
                l1=l1.next
            
            if l2:
                total+=l2.val
                l2=l2.next

            num=total%10
            carry=total//10

            curr.next=ListNode(num)
            curr=curr.next

        return dummy.next

'''
tc: O(n)
sc: O(n)

l1 = [1,2,3], l2 = [4,5,6]

carry=0
total=0

1 2 3    4 5 6
    l        L

total=3+6+0=9

num=9
carry=0

dummy-5-7-9

-------------------------------------
l1= 2 4 3  l2= 5 6 4
ans=807

2 4 3
5 6 4
8 0 7

carry=0
total=0

2 4 3    5 6 4
    l        L

total=3+4+1=8

num=8
carry=0

dummy-7-0-8

'''