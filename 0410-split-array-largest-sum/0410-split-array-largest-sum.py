class Solution:
    def getPartitions(self, arr: List[int], max_sum: int) -> int:
        partition=1
        sum_part=0
        for num in arr:
            if sum_part+num<=max_sum:
                sum_part+=num
            else:
                partition+=1
                sum_part=num
        return partition

    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=low+((high-low)>>1)
            s=self.getPartitions(nums,mid)
            if s>k:
                low=mid+1
            else:
                high=mid-1
        return low