# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower=float('-inf')
        upper=float('inf')

        def dfs(root,lower,upper):
            if root is None:
                return True

            if not lower<root.val<upper:
                return False

            return dfs(root.left,lower,root.val) and dfs(root.right,root.val,upper)


        return dfs(root,lower,upper)

'''
tc: O(n)
sc: O(h)

Input: root = [2,1,3]

dfs(2,-inf,inf) -- T&&T==return True
    -inf<2<inf
        left=dfs(1,-inf,2)
            -inf<1<2? yes
                left and right=none ---- return True
        right=dfs(3,2,inf)
            2<3<inf? yes
                left and right=none---return True
-----------------------------------------------------------------------------------

Input: root = [5,1,4,null,null,3,6]

dfs(5,-inf,inf) --  - T && F return False
    -inf<5<inf? yes
        left=dfs(1,-inf,5)--T
            -inf<1<5?yes
                left and right=none-- return True
        right=dfs(4,5,inf) -- F
        5<4<inf? false-- retrun False



'''





#         self.prev=None

#         def dfs(root):
#             if not root:
#                 return True

#             if not dfs(root.left):
#                 return False

#             if self.prev is not None and root.val<=self.prev:
#                 return False
            
#             self.prev=root.val

#             if not dfs(root.right):
#                 return False

#             return True

#         return dfs(root)
        

# '''
# tc: O(n)
# sc: O(h)
# inorder traversal
# left<root<right

# Input: root = [2,1,3] 

# dfs(2) 
# prev=None

#     left=dfs(1,none) -- T
#         1>=none? yes
#         prev=1
#         left=none
#         right=none

#     dfs(2)-- 2>=1 yes

#     right=dfs(3,none) -- T
#         3>=1? yes
#         prev=3
#         left=none
#         right=none


# ----------------------------------------------------------------
# Input: root = [1,2,3]

# dfs(1)
# prev=none
#     left=dfs(2,none)
#         2>=none? yes
#         prev=2

#     dfs(1) 1>=2 no return false no need to check right

#     right=dfs(3,none)
# -----------------------------------------------------------------

# Input: root = [5,1,4,null,null,3,6]

# dfs(5)
# prev=none

#     left=dfs(1)
#     1>=none?
#     prev=1

#     dfs(5)==5>=1? yes
#     prev=5

#     right=dfs(4)
#         left=dfs(3)
#             3>=5
#             return False


# '''