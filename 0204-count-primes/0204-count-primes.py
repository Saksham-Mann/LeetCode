class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        s=n//2
        is_prime=[True]*s
        is_prime[0]=False
        for i in range(1,int(n**0.5)//2+1):
            if is_prime[i]:
                p=2*i+1
                start=(p*p)//2
                is_prime[start::p]=[False]*len(is_prime[start::p])
        return 1+sum(is_prime)