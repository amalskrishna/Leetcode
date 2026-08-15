class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        win=len(needle)
        c=0
        while c+win<=len(haystack):
            if haystack[c:c+win]==needle:
                return c
            c+=1
        return -1