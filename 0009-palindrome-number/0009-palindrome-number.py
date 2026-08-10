class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp=0
        og=x
        while(x):
            rem=x%10
            temp=temp*10+rem
            x=x//10
        return og==temp