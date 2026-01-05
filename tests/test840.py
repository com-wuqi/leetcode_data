from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        y_size = len(grid)
        x_size = len(grid[0])
        if x_size<3 or y_size<3:
            return 0
        ans = 0
        position_5 = []
        for y in range(1,y_size-1):
            for x in range(1,x_size-1):
                if grid[y][x] == 5:
                    position_5.append([y,x])
                    # print(f"{y},{x}")
        for c in position_5:
            # y=c[0] x=c[1]
            if grid[c[0]+1][c[1]] + grid[c[0]-1][c[1]] == 10 and grid[c[0]][c[1]+1] + grid[c[0]][c[1]-1] == 10 and grid[c[0]+1][c[1]+1] + grid[c[0]-1][c[1]-1] == 10 and grid[c[0]-1][c[1]+1] + grid[c[0]+1][c[1]-1] == 10:
                ans+=1

        return ans
    
slu=Solution()
test1=slu.numMagicSquaresInside([[4,7,8],[9,5,1],[2,3,6]])
print(test1)
