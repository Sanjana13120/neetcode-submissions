# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root=TreeNode(preorder[0])
        root_idx=inorder.index(root.val)
        left_size=len(inorder[:root_idx])

        root.left=self.buildTree(preorder[1:left_size+1], inorder[:root_idx])
        root.right=self.buildTree(preorder[left_size+1:],inorder[root_idx+1:])

        return root
        

'''
TC: O(n²)
SC: O(n)

pre - 1 2 3 4
in  - 2 1 3 4

pre - root<left<right
in  - left<root<right

using preorder we know that 1 is the root node
so check whr 1 is in inorder 

so all val from pre[:idx of 1] are left subtree
and all val from pre[idx+1:] are right subtree


pre_start = 0
pre_end   = len(preorder)-1 =3
in_start  = 0
in_end    = len(inorder)-1 =3
root=preorder[0] =1
root_idx= index(inorder[root]) = 1 
left_size = len(inorder[:root_idx])=1

root_idx → used to split inorder
left_size → used to split preorder
      
      0   1   2  3
pre - 1 | 2 | 3  4
in  - 2 | 1 | 3  4

left:
preorder → [2]
inorder  → [2]

right:
preorder → [3, 4]
inorder  → [3, 4]

left=preorder[1:left_size+1], inorder[:root_idx]
right=preorder[left_size+1:],inorder[root_idx+1:]

'''