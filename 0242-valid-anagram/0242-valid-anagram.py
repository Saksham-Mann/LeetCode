class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=[0]*26
        if len(s)!=len(t):
            return False
        for i in s:
            arr[ord(i)-ord('a')]+=1
        for j in t:
            arr[ord(j)-ord('a')]-=1
        for i in arr:
            if i!=0:
                return False
        return True