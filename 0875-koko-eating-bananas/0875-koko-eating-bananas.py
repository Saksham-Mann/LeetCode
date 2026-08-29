class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        maxPile=max(piles)
        high=maxPile
        ans=maxPile
        while low<=high:
            mid=(low+high)//2
            th=0
            for i in piles:
                th+=math.ceil(i/mid)
            if th<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans