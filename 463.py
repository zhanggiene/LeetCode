class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        sum=0
        horizontal=len(grid)
        vertical=len(grid[0])
        for i in range(horizontal):
            for j in range(vertical):
                if grid[i][j]==1:
                    print(i,j)
                    sum+=4
                    if i-1>=0  and grid[i-1][j]==1:
                        sum-=1
                    if i+1<horizontal and grid[i+1][j]==1:
                        sum-=1
                    if j-1>=0 and grid[i][j-1]==1:
                        sum-=1
                    if j+1<vertical and grid[i][j+1]==1:
                        sum-=1
                print(sum)
        return sum
                