class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l=list(s)
        for i in t:
            if i not in l:
                return i
            l.remove(i)