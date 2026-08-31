class Solution:
    def getMax(self, mat: List[List[int]],col: int)->int:
        i=0
        for j in range(1,len(mat)):
            if mat[i][col]<mat[j][col]:
                i=j
        return i

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            row=self.getMax(mat,mid)
            left=mat[row][mid-1] if mid-1>=0 else -1
            right=mat[row][mid+1] if mid+1<n else -1
            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]
            elif mat[row][mid]<left:
                high=mid-1
            elif mat[row][mid]<right:
                low=mid+1
        return [-1,-1]
