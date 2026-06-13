class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1=set(nums)
        list1=list(set1)
        nums.sort()
        list1.sort()
        if(list1==nums):
            return False
        return True
        