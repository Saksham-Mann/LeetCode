class Solution:
    def p(self, x: int, n: int) -> int:
        if x==1 or n==0:
            return 1
        if n&1==0:
            return self.p((x*x)%1000000007,n//2)
        return (x*(self.p(x,n-1)))%(1000000007)
    def countGoodNumbers(self, n: int) -> int:
        prime=n//2
        even=(n+1)//2
        return (self.p(5,even)*self.p(4,prime))%(1000000007)