class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        r = len(matrix)
        c = len(matrix[0])


        for i in range(r):
            for j in range(i+1,c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

            
'''
tc: O(n**2)
Transpose: O(n**2)
Reverse each row:  O(n**2)
Combined:  O(n**2) + O(n**2) = O(n**2)

sc: O(1)

goal - rotate it by 90 degrees clockwise.

Approach:
1. transpose the matrix
2. reverse each row

Input: matrix = [[1,2], [3,4]]

  0 1
0 1 2
1 3 4

transpose

  0 1
0 1 3
1 2 4

reverse

  0 1
0 3 1
1 4 2

-------------------------------------------------------------------------------------------------------------------

Input: matrix = [[1,2,3], [4,5,6], [7,8,9]]

1 2 3
4 5 6
7 8 9

transpose
1 4 7
2 5 8
3 6 9

reverse each row
7 4 1
8 5 2
9 6 3


'''