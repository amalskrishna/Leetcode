class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        j=1
        i=0
        res=[]
        res.append(words[i])
        while j<len(words):
            if sorted(words[j])!=sorted(words[i]):
                res.append(words[j])
            i+=1
            j+=1
        return res