class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        firstrowzero = False
        firstcolzero = False

        # Step 1: Check first column
        for r in range(rows):
            if matrix[r][0] == 0:
                firstcolzero = True

        # Step 2: Check first row
        for c in range(cols):
            if matrix[0][c] == 0:
                firstrowzero = True

        # Step 3: Mark rows and columns
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Step 4: Update inner matrix
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 5: Update first row
        if firstrowzero:
            for c in range(cols):
                matrix[0][c] = 0

        # Step 6: Update first column
        if firstcolzero:
            for r in range(rows):
                matrix[r][0] = 0


"""  
tc: O(m*n)
sc: O(1)
        
goal - if an element is 0, set its entire row and column to 0's. update matrix in place

Approach (Optimal - O(1) Extra Space)

1. Initialize two boolean variables firstrowzero and firstcolzero to track whether the original first row and first column contain zero.
2. Traverse the first column. If any element is zero, set firstcolzero = True.
3. Traverse the first row. If any element is zero, set firstrowzero = True.
4. Traverse the remaining matrix (excluding first row and first column). If an element is zero:
        Mark its row by setting matrix[r][0] = 0.
        Mark its column by setting matrix[0][c] = 0.
5. Traverse the inner matrix again. If matrix[r][0] == 0 OR matrix[0][c] == 0, set matrix[r][c] = 0.
6. If firstrowzero is True, make the entire first row zero.
7. If firstcolzero is True, make the entire first column zero.

-------------------------------------------------------------------------------------------------------------

Input: matrix = [[1,2,3], [4,0,5], [6,7,8]]
  
  0 1 2
0 1 2 3
1 4 0 5 
2 6 7 8

firstrowzero=F 
firstcolzero=F

loop over rows and cols and check if first row or first col==0 no

mat[1][1]==0
    mat[r][0]=0  (1,0)
    mat[0][c]=0  (0,1)

mat[r][0]==0 or mat[0][c]==0
    mat[1][0]==0 so mat[1][0], mat[1][1], mat[1][2]==0
    and simlarly
    mat[0][1]==0? so mat[0][1] = mat[1][1] = mat[2][1]==0


  0 1 2
0 1 0 3
1 0 0 0
2 6 0 8


"""
