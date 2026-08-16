# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q=deque([root])
        ans=[]
        

        while q:
            currlvl=[]
            
            for _ in range(len(q)):
                node=q.popleft()
                currlvl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(currlvl)

        return ans


'''
tc: O(n)
sc: O(n)
we will use BFS DS here using a Queue

initially append root to Q

q={1}

i=0

while q:
    currlvl=[]
    loop until len(q)
        node=q.popleft()
        then append node to currlevl
        then loop check its left and right and append to Q 

    finally append currlvl to ans
            

q={2 3}
currlv=[[1]]

next pop 2 Q={3}

node=2 
q={3 4 5}
currlvl=[2]

node=3 
q={4 5 6 7}
currlvl=[2,3]

ans=[[1],[2,3]]

node=4 
q={5 6 7}
currlvl=[4]

noed=5 then 6 then 7
q={}
currlvl=[4 5 6 7]

ans=[[1],[2,3],[4,5,6,7]]


'''