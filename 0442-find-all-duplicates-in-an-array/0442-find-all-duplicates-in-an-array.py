class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            ind=abs(i)-1
            if nums[ind]<0:
                res.append(abs(i))
            else:
                nums[ind]*=-1
        return res


