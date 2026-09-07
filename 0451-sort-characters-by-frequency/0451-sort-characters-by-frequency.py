class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        s=sorted(d.keys(),key=d.get,reverse=True)
        return "".join(i*d[i] for i in s)