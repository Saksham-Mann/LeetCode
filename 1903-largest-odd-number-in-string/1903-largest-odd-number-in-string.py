class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if (int(num[i])&1==1):
                ind=i
                return num[0:ind+1]
        return ""