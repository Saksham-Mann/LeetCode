class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        r=1<<n
        ans=[]
        for num in range(r):
            subset=[]
            for i in range(n):
                if num&(1<<i):
                    subset.append(nums[i])
            ans.append(subset)
        return ans