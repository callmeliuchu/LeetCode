class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        return self.count(grid)

        
    def is_legal(self,grid,i,j,visited,tag):
        m = len(grid)
        n = len(grid[0])
        if i>=0 and i<m and j>=0 and j<n and grid[i][j] == tag and (i,j) not in visited:
            return True
        return False

    def get_around(self,grid,i,j,visited,tag):
        ret_arr = []
        for k in [-1,1]:
            if self.is_legal(grid,i+k,j,visited,tag):
                ret_arr.append((i+k,j))
            if self.is_legal(grid,i,j+k,visited,tag):
                ret_arr.append((i,j+k))
        return ret_arr

    def dfs(self,grid,i,j,visited,tag):
        if (i,j) in visited:
            return
        visited.add((i,j))
        around_arr = self.get_around(grid,i,j,visited,tag)
        for i1,j1 in around_arr:
            self.dfs(grid,i1,j1,visited,tag)


    def count(self,grid):
        res = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    self.dfs(grid,i,j,visited,'1')
                    res += 1
        return res