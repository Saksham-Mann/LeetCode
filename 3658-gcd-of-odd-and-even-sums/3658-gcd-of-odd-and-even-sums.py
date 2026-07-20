class Solution:
    def findgcd(self,n1: int,n2: int) -> int:
        while (n1>0 and n2>0):
            if (n1>n2):
                n1=n1%n2
            else:
                n2=n2%n1
        if (n1==0):
            return n2
        return n1
    
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=(n*(2+2*(n-1)))//2
        even=(n*(4+2*(n-1)))//2
        return self.findgcd(odd,even)