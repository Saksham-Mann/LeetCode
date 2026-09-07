class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=min(strs)
        last=max(strs)
        ans=[]
        for i in range(min(len(first),len((last)))):
            if first[i]!=last[i]:
                return ''.join(ans)
            ans.append(first[i])
        return ''.join(ans)