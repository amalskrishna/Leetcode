class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeated = -1

        #repeated number
        for i in grid:
            for j in i:
                if j in seen:
                    repeated = j
                seen.add(j)

        #missing number
        total_numbers = n * n
        missing = -1

        for i in range(1, total_numbers + 1):
            if i not in seen:
                missing = i
                break

        return [repeated, missing]

