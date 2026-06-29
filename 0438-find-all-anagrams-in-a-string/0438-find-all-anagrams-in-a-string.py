class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        cntp=defaultdict(int)
        window=defaultdict(int)
        for i in range(len(p)):
            cntp[p[i]]+=1
            window[s[i]]+=1
        ans=[]
        if cntp==window:
            ans.append(0)
        for i in range(len(p),len(s)):
            left=s[i-len(p)]
            right=s[i]
            window[left]-=1
            if(window[left]==0):
                del window[left]
            window[right]+=1
            if window==cntp:
                ans.append(i-len(p)+1)
        return ans
