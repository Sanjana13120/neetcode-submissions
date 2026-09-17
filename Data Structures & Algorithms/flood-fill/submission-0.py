class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org_color = image[sr][sc]

        if org_color == color:
            return image

        r=len(image)
        c=len(image[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or image[i][j]!=org_color:
                return 

            image[i][j]=color

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        dfs(sr,sc)

        return image 

'''
tc: O(r*c)
sc: O(r*c)


sr = 1, sc = 1, color = 2

  0 1 2 
0 1 1 1
1 1 1 0
2 1 0 1

approach: dfs

1. so first we need to start with starting pixel img[sr][sc]
2. if img[sr][sc] color is already equal to color, no changes return image
3. run dfs(sr,sc)
4. if out of boundary or image[sr][sc]!= org color return 
5. mark the img[sr][sc] with new color and check up, down, left, right and explore dfs

org_color = img[1][1] = 1

dfs(1,1)
    mark with new color 2
    up - dfs(0,1)
        1==1 so mark with new color 2
            up- X
            right - dfs(0,2)
                 1==1 mark as 2
                 up, right- x
                 left already 2
                 down is 0 no change
            down - already 2
            left - dfs(0,0)
                1==1 mark it as 2
                    up, left- x
                    right- 2 already
                    down- dfs(1,0)
                        1==1 mark it as 2
                            up,right-already markded
                            left-x
                            down- (2,0)
                                1==1 mark it as 2
                                up- marked
                                left,down -x
                                right -0 no change
    down - 0 no chanhge
    left - already marked
    right - 0 no change
    

  0 1 2 
0 2 2 2
1 2 2 0
2 2 0 1


Output: [[2,2,2],[2,2,0],[2,0,1]]

------------------------------------------------------------------------------------------------
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

org_color = image[0][0]=0 == color so no change




'''