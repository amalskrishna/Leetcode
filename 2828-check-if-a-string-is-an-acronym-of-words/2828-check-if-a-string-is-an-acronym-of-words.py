class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words)!=len(s):
            return False
        for i in range(0,len(s)):
            if s[i]!=words[i][0]:
                return False
        return True

        