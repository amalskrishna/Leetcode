class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        cnts=defaultdict(int)
        window=defaultdict(int)
        for i in s1:
            cnts[i]+=1
        for i in range(len(s1)):
            window[s2[i]]+=1
        if window==cnts:
            return True
        for i in range (len(s1),len(s2)):
            window[s2[i]]+=1
            left=s2[i-len(s1)]
            window[left]-=1
            if window[left]==0:
                del window[left]
            if window==cnts:
                return True
        return False