class Solution:
    def isPossible(self,arr: List[int], mid: int,m: int, k: int)->bool:
        count=0
        bouquet=0
        for i in arr:
            if i<=mid:
                count+=1
                if count==k:
                    bouquet+=1
                    count=0
            else:
                count=0
        return bouquet>=m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans=-1
        low=1
        high=max(bloomDay)
        while low<=high:
            mid=low+((high-low)>>1)
            if self.isPossible(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans