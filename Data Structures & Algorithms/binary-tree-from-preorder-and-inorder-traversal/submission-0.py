# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={val:idx for idx,val in enumerate(inorder)}

        self.pre_idx=0
        def dfs(start,end):
            if start>end:
                return None

            root=TreeNode(preorder[self.pre_idx])
            self.pre_idx+=1
            mid=inorder_map[root.val]
            root.left=dfs(start,mid-1)
            root.right=dfs(mid+1,end)

            return root

        return dfs(0,len(preorder)-1)


'''
tc: O(n)
sc: O(n)

preorder = [1,2,3,4], inorder = [2,1,3,4]

index_map={2:0 1:1 3:2 4:3}

      0   1   2  3
pre - 1 | 2 | 3  4
in  - 2 | 1 | 3  4

root_idx=0

dfs(0,3):
    start=0 end=3
    0<3:
        root=preorder[root_idx]=1
        root_idx+=1 --->1
        mid=index_map[1]=1
        root.left=dfs(0,0)
            0>0? no
            root=preorder[1]=2
            root_idx=2
            mid=index_map[2]=0
            root.left=dfs(0,-1) = none 
            root.right=dfs(1:0) = none
        root.right=dfs(2,3)
            2>3: no
            root=preorder[root_idx]=3
            root_idx+=1--3
            mid=index_map[root]=indexmap[3]=2
            root.left=dfs(2,1) 
                2>1? retrun None
            root.right=dfs(3,3)   
                3>3
                root=preorder[3]  =4
                root_idx=4
                mid=indexmap[4]=3
                root.left=dfs(3,2)--none
                root.right=dfs(4,3)--none


        1
    2      3
       null   4

'''


