# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float('-inf')

        def dfs(root):
            if not root:
                return 0

            leftsum=max(0,dfs(root.left))
            rightsum=max(0,dfs(root.right))

            self.maxsum=max(self.maxsum,leftsum+rightsum+root.val)

            return max(leftsum,rightsum)+root.val

        dfs(root)
        return self.maxsum
        

'''
tc: O(n)
sc: O(h)

root = [-15,10,20,null,null,15,5,-5]

dfs(-15)
    leftsum=max(dfs(10),0) - 10
        left and right are none - return 0
        maxsum=max(10+0+0,-inf)=10
        return max(0,0)+10 =10

    rightsum=max(dfs(20),0) - 30

        leftsum=dfs(15)  - 15
            leftsum=max(dfs(-5),0)=max(-5,0)=0
                left and right are none - return 0
                
                rightsum=0
                maxsum=max(10,0+0-5)=10
                return max(0,0)-5 =-5

            maxsum=max(10,0+0+15)=15
            return max(0,0)+15=15
        

        rightsum=max(dfs(5),0) = 5
            left and right are none - return0
            maxsum=max(15,0+0+5)=15
            return max(0,0)+5=5

        
        maxsum=max(15,15+5+20)=40
        return max(15,5)+20=35

    maxsum=max(40,10+35-15)=40
    return max(10,35)-15=20







'''