class Solution:
    def toLowerCase(self, s: str) -> str:
        res=""
        for i in s:
            if "A"<=i<="Z":
                res+=chr(ord(i)+32)
            else:
                res+=i
        return res