# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(root):
            if not root:
                res.append("N")
                return 
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        #print(",".join(res))
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr=data.split(",")
        self.i=0
        print(arr)
        def dfs():
            if arr[self.i]=="N":
                self.i+=1
                return None
            
            node=TreeNode(int(arr[self.i]))
            self.i+=1

            node.left=dfs()
            node.right=dfs()
            return node        
        
        return dfs()

'''
tc: O(n)
sc: O(n)

serialization - convert BT to string
[1 2 N N 3 4 N N 5 N N]

we can use dfs -- preorder root<left<right
if child node - then "N"

deserialization - convert string to BT

now we have [1 2 N N 3 4 N N 5 N N]

'1', '2', 'N', 'N', '3', '4', 'N', 'N', '5', 'N', 'N'
                                        i


[1 2 3 null null 4 5] 

'''