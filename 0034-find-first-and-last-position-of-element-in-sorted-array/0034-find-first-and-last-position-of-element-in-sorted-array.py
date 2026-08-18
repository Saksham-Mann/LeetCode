class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bi(ff: bool):
            low=0
            high=len(nums)-1
            res=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    res=mid
                    if ff:
                        high=mid-1
                    else:
                        low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return res
        first=bi(ff=True)
        if first==-1:
            return [-1,-1]
        second=bi(ff=False)
        return [first,second]