# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxsofar):
            count=0

            if root is None:
                return 0

            if root.val>=maxsofar:
                count=1

            maxsofar=max(maxsofar,root.val)

            left=dfs(root.left,maxsofar)
            right=dfs(root.right,maxsofar)

            return count+left+right        

        return dfs(root, root.val)
        

'''
tc: O(n)
sc: O(h)

we can use dfs here
we have to check if node is good meaning no node should be greater than X from root to node X 

Input: root = [2,1,1,3,null,1,5]


dfs(2,2) = 1+1+1=3
count=0
root=2 maxsofar=2
if root>=maxsofar -- 2>=2
count=1

left=dfs(1,2)= 1
        dfs(1,2)
        1>=2?
        maxsofar=max(2,1)=2

        left=dfs(3,2) = 1
        right=dfs(none,2)=0

        dfs(3,2)
        3>=2? count=1
        maxsofar=max(2,3)=3

right=dfs(1,2)=0+0+1=1
    count=0
     1>=2? no
     maxsofar=2
     
     left=dfs(1,2) = 0+0+0=0
            1>=2? no
            maxsofar=2
            left=0
            right=0
     right=dfs(5,2) = 1+0+0=1
            5>=2? yes
            count=1
            maxsofar=5
            left=0
            right=0


---------------------------------------------------------------------
Input: root = [1,2,-1,3,4]

dfs(1,1) = 1+3+0===4--->return 4
count=0
1>=1? count=1
maxsofar=1
left=dfs(2,1)=1+1+1=3
        2>=1? yes 
        count=1
        maxsofar=2
        left=dfs(3,2) = 1+0+0=1
            3>=2? count=1
            maxsofar=3
            left=0
            right=0

        right=dfs(4,2)=1+0+0=1
            4>=2? count=1
            maxsofar=4
            left=0
            right=0


right=dfs(-1,1)=0+0+0=0
    count=0
    -1>=1? no
    left=0
    right=0

'''