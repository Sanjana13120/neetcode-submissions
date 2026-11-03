class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        cols = set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(m):
            for c in range(n):
                if r in rows or c in cols:
                    matrix[r][c] = 0


"""
tc: O(m*n)
sc: O(m+n)

goal - if an element is 0, set its entire row and column to 0's. update matrix in place


Input: matrix = [ [0,1], [1,0]]

  0 1
0 0 1
1 1 0

mat[0][0]==0
    rows={0} cols={0}
    
mat[1][1]=0
    rows={0,1} cols={0,1}

loop over each cell

r=0 c=0 both in rows and cols mat[0][0]=0
r=0 c=1 both in rows and cols mat[0][1]=0

r=1 c=0 both in rows and cols mat[1][0]=0
r=1 c=1 both in rows and cols mat[1][1]=0


  0 1
0 0 0
1 0 0

-------------------------------------------------------------------------------------------------------------

Input: matrix = [[1,2,3], [4,0,5], [6,7,8]]
  
  0 1 2
0 1 2 3
1 4 0 5 
2 6 7 8

row = {} 
cols = {}

mat[1][1]=0
row = {1} 
cols = {1}

loop over all cell

r=0 c=0
r=0 c=1 1 in cols   so mat[0][1]=0
r=0 c=2

r=1 c=0 1 in rows so mat[1][0]=0
r=1 c=1 1 in rows or 1 in cols so mat[1][1]=0
r=1 c=2 1 in rows so mat[1][2]=0

r=2 c=0
r=2 c=1 1 in cols so mat[2][1]=0
r=2 c=2 

  0 1 2
0 1 0 3
1 0 0 0
2 6 0 8






"""
