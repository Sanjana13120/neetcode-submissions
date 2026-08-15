# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None

        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)

        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)

        return root
        

'''
tc: O(h)
sc: O(h)

5 3 8 1 4 7 9 null 2


p=3 q=8

root=5
3<5 adn 8<5? false
3>5 and 8>5? return false
return root=5

-------------------------------------------

root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

root=5
3<5 and 4<5?
move left

root=3
3<3 and 4<3? false
3>3 and 4<3? false
return root=3



'''