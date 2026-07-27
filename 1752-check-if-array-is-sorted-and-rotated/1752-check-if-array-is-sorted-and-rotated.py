class Solution:
    def check(self, nums: List[int]) -> bool:
        large=0
        for i in range(len(nums)):
            if (nums[i]>nums[(i+1)%len(nums)]):
                large+=1
        return large<=1