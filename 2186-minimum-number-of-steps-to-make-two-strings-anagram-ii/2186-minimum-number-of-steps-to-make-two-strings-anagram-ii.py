class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnts=defaultdict(int)
        cntt=defaultdict(int)
        for i in s:
            cnts[i]+=1
        for i in t:
            cntt[i]+=1
        cnt=0
        for i in set(cnts)|set(cntt):
            cnt+=abs(cnts[i]-cntt[i])
        return cnt