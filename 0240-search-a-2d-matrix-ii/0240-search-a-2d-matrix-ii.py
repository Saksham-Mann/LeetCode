class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        column=len(matrix[0])-1
        n=len(matrix)
        while row<n and column>=0:
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                row+=1
            else:
                column-=1
        return False