class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        num=0
        for i in range(len(nums)):
            if (count==0):
                count=1
                num=nums[i]
            elif (nums[i]==num):
                count+=1
            else:
                count-=1
        return num