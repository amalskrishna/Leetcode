class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        n=0
        for i in nums:
            if i%3==0 and i%2==0:
                sum+=i
                n+=1
        avg= 0 if n==0 else sum//n
        return avg