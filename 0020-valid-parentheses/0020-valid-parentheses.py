class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in s:
            if i in "([{":
                top+=1
                stack.append(i)
            else:
                if (top==-1):
                    return False
                last=stack[top]
                top-=1
                stack.pop()
                if ((last!="(" and i==")") or (last!="[" and i=="]") or (last!="{" and i=="}") ):
                    return False
        return top==-1