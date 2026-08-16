# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q=deque([root])
        ans=[]

        while q:
            currlvl=len(q)
            for i in range(currlvl):
                node=q.popleft()

                if i==currlvl-1:
                    ans.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans
        

'''
TC: O(n)
SC: O(n)

Input: root = [1,2,3,null,4,null,5]

q={1}

currlvl=1
node=1 and i=0
0==0? ans=[1] 

q={2,3}
currlvl=2

i=0,1
node=2 and 0==1?no q={3,4}
node=3 and 1==1? yes q={4,5}
ans=[1,3]

q={4,5}
currlvl=2 i=0,1
node=4 and 0==1? no q={5}
node=5 and 1==1? yes q={}
ans=[1,3,5]

---------------------------------------------------
Input: root = [1,2,3,4,null,null,null,5]

q={1}

node=1
i=0  --- 0==0? yes 
ans=[1]

q={2,3}

node=2 and i=0,1
i=0 -- 0==1? no
q={3,4}

node=3
i=1 -- 1==1? yes 
ans=[1,3]

q={4}
node=4 and i=0
i=0 0==0?
ans=[1,3,4]
q={5}

node=5 and i=0, q={}
0==0? yes ans=[1,3,4,5] 






'''