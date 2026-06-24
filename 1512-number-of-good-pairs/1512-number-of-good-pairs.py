class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        cnt=0
        for val in nums:
            cnt+=dic[val]
            dic[val]+=1
        return cnt