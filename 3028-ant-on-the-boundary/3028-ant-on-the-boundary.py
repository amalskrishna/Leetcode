class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos=0
        cnt=0
        for i in nums:
            pos+=i
            if pos==0:
                cnt+=1
        return cnt