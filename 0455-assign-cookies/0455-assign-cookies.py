class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt=0
        g.sort()
        s.sort()
        x=0
        y=0
        while x<len(g) and y<len(s):
            if s[y]>=g[x]:
                cnt+=1
                x+=1
                y+=1
            else:
                y+=1
        return cnt