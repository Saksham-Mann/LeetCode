class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=prices[0]
        mp=0
        for i in range(1,len(prices)):
            if (prices[i]<mi):
                mi=prices[i]
            else: 
                mp=max(mp,prices[i]-mi)
        return mp