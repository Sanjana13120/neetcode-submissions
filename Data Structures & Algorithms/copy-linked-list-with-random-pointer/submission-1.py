"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        copy={}

        while curr:
            copy[curr]=Node(curr.val)
            curr=curr.next

        curr=head
        
        while curr:
            copy[curr].next=copy.get(curr.next)
            copy[curr].random=copy.get(curr.random)
            curr=curr.next

        return copy[head]


'''
Time:  O(n)
Space: O(n)

org= [3 7 4 5]

3-->7-->4-->5

3.random=None
7.random=5
4.random=3
5.random=7

copy={3:3', 7:7', 4:4', 5:5'}

3'-->7'-->4'-->5'

3'.random=null
7'.random=5'
5'.random=3'
3'.random=7'

'''