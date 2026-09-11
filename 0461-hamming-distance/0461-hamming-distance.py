class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        num=x^y
        for i in range(32):
            count+=(num&1)
            num>>=1
        return count