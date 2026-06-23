class Solution:
    def minPartitions(self, n: str) -> int:
        maxnum=0
        for i in n:
            if int(i) > maxnum:
                maxnum=int(i)
        return maxnum