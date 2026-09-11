class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m=1000000007
        prime=n//2
        even=(n+1)//2
        return (pow(5,even,m)*pow(4,prime,m))%m