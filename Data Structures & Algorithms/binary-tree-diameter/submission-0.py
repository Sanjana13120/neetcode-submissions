# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0

        def dfs(root):

            if root is None:
                return 0

            left=dfs(root.left)
            right=dfs(root.right)

            self.diameter=max(self.diameter,left+right)

            return 1+max(left,right)

        dfs(root)
        return self.diameter
 

'''

Height = number of nodes along the longest downward path.
Diameter = number of edges along the longest path between any two nodes.

tc: O(n)
sc: O(h)

Input: root = [1,null,2,3,4,5]

self.diameter=0
node 5: l=0 r=0 d=0 h=1
node 4: l=0 r=0 d=0 h=1
node 3: l=1 r=0 d=1 h=2
node 2: l=2 r=1 d=3 h=3
node 1: l=0 r=3 d=3 h=4

Longest path:  5 → 3 → 2 → 4



'''