class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums)>threshold:
            return -1
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)>>1
            s=sum(math.ceil(nums[i]/mid) for i in range(len(nums)))
            if s<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return low