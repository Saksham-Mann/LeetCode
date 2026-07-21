class Solution:
    def fib(self, n: int) -> int:
        if (n==0):
            return 0
        l=1
        s=0
        for i in range(n-1):
            output=l+s
            s=l
            l=output
        return l