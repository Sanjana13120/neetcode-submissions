# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.small=k

        def inorder(root):
            if not root:
                return None
                
            left=inorder(root.left)
            if left is not None:
                return left

            self.small-=1

            if self.small==0:
                return root.val
            
            right=inorder(root.right)
            if right is not None:
                return right


        return inorder(root)
        

'''
TC: O(n)
SC: O(h)

Input: root = [4,3,5,2,null], k = 4

2<3<4<5 return k-1 node

inorfer traversal?

small=k=4

dfs(4)-1
 small=2-1=1==0? x
    dfs(3) -- 2
     small=3-1=2==0? x
        dfs(2) -- 3
        small=4-1=3==0? x

    dfs(5)
    small=1-1=0==0? return 5
'''