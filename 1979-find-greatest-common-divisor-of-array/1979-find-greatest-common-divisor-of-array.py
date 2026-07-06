class Solution:
    def findGCD(self, nums: List[int]) -> int:
        for i in range(min(nums),0,-1):
            if max(nums)%i==0 and min(nums)%i==0:
                return i