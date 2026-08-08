class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        c1=0
        c2=0
        e1=float('-inf')
        e2=float('-inf')
        for i in range(len(nums)):
            if c1==0 and nums[i]!=e2:
                c1+=1
                e1=nums[i]
            elif c2==0 and nums[i]!=e1:
                c2+=1
                e2=nums[i]
            elif nums[i]==e1:
                c1+=1
            elif nums[i]==e2:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1=0
        c2=0
        for i in range(len(nums)):
            if nums[i]==e1:
                c1+=1
            if nums[i]==e2:
                c2+=1
        m=((len(nums))//3)+1
        if (c1>=m):
            result.append(e1)
        if (c2>=m and e1!=e2):
            result.append(e2)
        return result