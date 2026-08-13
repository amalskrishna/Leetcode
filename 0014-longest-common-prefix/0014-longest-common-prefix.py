class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        sor=sorted(strs)
        r=min(len(sor[0]),len(sor[-1]))
        for i in range(r):
            if sor[0][i]!=sor[-1][i]:
                return ans
            ans+=sor[0][i]
        return ans
