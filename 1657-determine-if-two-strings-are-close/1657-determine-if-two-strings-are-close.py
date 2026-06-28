class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1=defaultdict(int)
        cnt2=defaultdict(int)
        for i in word1:
            cnt1[i]+=1
        for i in word2:
            cnt2[i]+=1
        if cnt1.keys()==cnt2.keys() and sorted(list(cnt1.values()))==sorted(list(cnt2.values())):
            return True
        return False
