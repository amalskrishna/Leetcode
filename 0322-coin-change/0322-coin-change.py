class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dih = {}
        def solve(amt):
            if amt<0:
                return -1
            elif amt==0:
                return 0
            if amt in dih:
                return dih[amt]

            minc = float('inf')
            for i in coins:
                res = solve(amt-i)
                if res!=-1:
                    minc = min(res+1,minc)
            dih[amt] = minc if minc!=float('inf') else -1
            return dih[amt]
        return solve(amount)