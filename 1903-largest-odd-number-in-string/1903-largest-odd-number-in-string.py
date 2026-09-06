class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if num[i] in {'1','3','5','7','9'}:
                ind=i
                return num[0:ind+1]
        return ""