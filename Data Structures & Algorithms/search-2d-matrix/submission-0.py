class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = rows * cols - 1

        while start <= end:
            mid = start + (end - start) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                start = mid + 1

            else:
                end = mid - 1

        return False


"""
tc: O(log(m*n))
sc: O(1)
m - no of rows
n - no of cols

goal - Return true if target exists within matrix or false otherwise.

approach: binary search 

since each row is sorted 
and first row ele > last ele in prev row

so it becomes 1 2 4 8 10 11 12 14 20 30 40

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

0 1 2 3 4  5  6  7  8  9 10 11
1 2 4 8 10 11 12 13 14 20 30 40

rows=3
cols=4

start = 0
end = 11

mid = 5
row = mid//cols = 1
col = mid%cols  = 1 

mat[1][1]=11>10

start=0 end=4
mid=2
row=0
col=2

4<10? strt=3 end=4

mid=3
row=0
col=3
8<10 > start=4 end=4

mid=4
row=1
col=0
mat[1][0]=10==10?return true




"""
