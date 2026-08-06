class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        sum=0
        p={}
        p[0]=1
        n=len(nums)
        for i in range(n):
            sum+=nums[i]
            r=sum-k
            if (r in p):
                count+=p[r]
            p[sum]=p.get(sum,0)+1
        return count