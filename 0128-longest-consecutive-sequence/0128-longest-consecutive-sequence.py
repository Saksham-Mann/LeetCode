class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if (n==0):
            return 0
        longest=1
        s=set()
        for i in nums:
            s.add(i)
        for i in s:
            if i-1 not in s:
                count=1
                x=i
                while x+1 in s:
                    x=x+1
                    count+=1
                longest=max(longest,count)
        return longest