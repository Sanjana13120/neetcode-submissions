# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,curr,end):
        prev=None

        while curr!=end:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail=head

        for _ in range(k):
            if not tail:
                return head

            tail=tail.next

        rev=self.reverse(head,tail)

        head.next=self.reverseKGroup(tail,k)

        return rev       
        

'''
tc: O(n)
sc: O(n/k)

1 2 3 4 5 6   k=3
h
      t

head=1
tail=4

reverse(1,4)
curr=1
end=4
prev=None

curr!=end

3-2-1-None

curr=4
prev=3
nxt=4

rev=3-2-1-None

1.next=reversegroup(4,3)

4 5 6 
    t
h

reverse(4,None)

curr=4  end=none

6-5-4-none

curr=none
nxt=none
prev=6

1.next=6-5-4-none

3-2-1-6-5-4-none

------------------------------------------------------

1 2 3 4 5 k=3
h
      t

3-2-1-none

1.next=reversegroup(4,3)

4-5-none
h
     t
if tail is none we have to return none 
meaning if check whether there are k nodes
3-2-1-4-5-none


'''