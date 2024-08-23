import collections
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        m = collections.defaultdict(int)
        cnt = 0

        for row in grid:
            m[str(row)] += 1
        
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += m[str(col)]
        return cnt
        
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(Solution().equalPairs(grid))