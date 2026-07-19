class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        while True:
            temp=0
            for i in str(n):
                temp+=int(i)**2
            if temp in l:
                return False
            if temp==1:
                return True
            l.append(temp)
            n=temp
        
