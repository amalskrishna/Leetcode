class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        res=[0,0]
        for i in nums:
            d[i]+=1
        for i in range(1,len(nums)+1):
            if d[i]==2:
                res[0]=i
            elif d[i]==0:
                res[1]=i
        return res

