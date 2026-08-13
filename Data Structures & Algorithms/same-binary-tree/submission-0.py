# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if not p or not q:
            return False

        if p.val!=q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        
        

'''
for same tree we have to check structure
left and right val should be equal -- True
both child =none -->True
if one none other has value --then false
otherwise --> compare left AND right

tc: O(n)
sc: O(h)

'''