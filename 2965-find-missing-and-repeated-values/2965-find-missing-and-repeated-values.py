class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=len(grid)
        sum1=0
        sumsq=0
        n=l*l
        for i in grid:
            for j in i:
                sum1 +=j
                sumsq +=j*j
        exsum=(n*(n+1))//2
        exsumsq= n*(n+1)*(2*n+1)//6

        diff=sum1-exsum
        diffsq=sumsq-exsumsq
        
        sumxy = diffsq//diff
        
        repeated= (diff+sumxy)//2
        missing=repeated-diff
        return [abs(repeated),abs(missing)]

