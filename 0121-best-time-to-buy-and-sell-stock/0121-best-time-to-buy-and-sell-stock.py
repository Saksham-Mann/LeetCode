class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=float('inf')
        mp=0
        for i in range(len(prices)):
            if (prices[i]<mi):
                mi=prices[i]
            else: 
                mp=max(mp,prices[i]-mi)
        return mp