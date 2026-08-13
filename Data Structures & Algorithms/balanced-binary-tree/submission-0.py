# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0

            left=dfs(root.left)
            right=dfs(root.right)


            if left==-1 or right==-1:
                return -1

            if abs(left - right)>1:
                return -1

            return 1+max(left,right)

        isbalanced=dfs(root)
        return True if  isbalanced!=-1 else False

'''
tc: O(n)
sc: O(1)

dfs(1)=3
left=dfs(2)=1
right=dfs(3)=2
abs(1-2)=1>1 returns 3

dfs(2)--left=0 right=0 --> return 1

dfs(3) =2
left=dfs(4)=1
right=0
abs(1-0)<1

dfs(4)=1

'''
        