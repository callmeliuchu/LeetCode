class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        graph = []
        for i in range(m):
            graph.append([0]*n)
        k = 0
        while k<n and obstacleGrid[0][k] != 1:
            graph[0][k] = 1
            k += 1
        k = 0
        while k<m and obstacleGrid[k][0] != 1:
            graph[k][0] = 1
            k += 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    a = 0
                    if obstacleGrid[i-1][j] != 1:
                        a = graph[i-1][j]
                    b = 0
                    if obstacleGrid[i][j-1] != 1:
                        b = graph[i][j-1]
                    graph[i][j] =  a + b
        return graph[-1][-1]