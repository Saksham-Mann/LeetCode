class Solution:
    def getTotal(self, arr: List[int], mid: int)->int:
        days=1
        load=0
        for w in arr:
            if load+w > mid:
                days+=1
                load=w
            else:
                load+=w
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=((low+high)>>1)
            total=self.getTotal(weights,mid)
            if total<=days:
                high=mid
            else:
                low=mid+1
        return low