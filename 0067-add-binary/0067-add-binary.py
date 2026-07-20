class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = len(a) - 1
        r = len(b) - 1
        carry = 0
        result = []
        while l >= 0 or r >= 0 or carry > 0:
            bit_a = int(a[l]) if l >= 0 else 0
            bit_b = int(b[r]) if r >= 0 else 0
            total = bit_a + bit_b + carry
            carry = total // 2
            result.append(str(total % 2))
            
            l -= 1
            r -= 1
        return "".join(reversed(result))