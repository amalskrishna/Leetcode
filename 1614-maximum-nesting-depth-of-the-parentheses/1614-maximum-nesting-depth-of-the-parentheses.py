class Solution:
    def maxDepth(self, s: str) -> int:
        l=[]
        max=0
        for i in s:
            if i=="(":
                l.append(i)
                if len(l)>max:
                    max=len(l)
            elif i==")":
                l.pop()
        return max