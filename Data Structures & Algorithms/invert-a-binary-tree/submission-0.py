# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None

        root.left,root.right=root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        

'''
tc: O(n)
sc: O(n)
1 2 3 4 5 6 7

preorder traversal
root
swap left and right and child node
left
right

1 3 2 7 6 5 4

'''