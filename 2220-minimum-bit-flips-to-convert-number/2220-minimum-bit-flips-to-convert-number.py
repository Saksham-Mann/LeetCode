class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        num=start^goal
        for i in range(32):
            count=count+(num&1)
            num=num>>1
        return count