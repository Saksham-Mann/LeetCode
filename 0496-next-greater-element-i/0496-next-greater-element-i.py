class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        s = []
        for num in nums2:
            while s and num > s[-1]:
                smaller = s.pop()
                d[smaller] = num
            s.append(num)
        return [d.get(x, -1) for x in nums1]