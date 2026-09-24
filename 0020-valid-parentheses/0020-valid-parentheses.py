class Solution:
    def isValid(self, s: str) -> bool:
        top=-1
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
                top+=1
            if i==')' or i=='}' or i==']':
                if top==-1:
                    return False
                
                if (i==')' and stack[top]=='(') or (i==']' and stack[top]=='[') or(i=='}' and stack[top]=='{'):
                    top-=1
                    stack.pop()
                else:
                    return False
        return top==-1