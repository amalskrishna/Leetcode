class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        l,r=0,n-1
        k=n-1
        while l<=r:
            if(abs(nums[l]) > abs(nums[r])):
                res[k]=nums[l]**2
                l+=1
            else:
                res[k]=nums[r]**2
                r-=1
            k-=1
        return res
        