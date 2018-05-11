<<<<<<< HEAD
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
=======
import numpy as np
obstacleGrid =[[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
def isLegal(i,j,m,n):
	return i>=0 and i<m and j>=0 and j<n and obstacleGrid[i][j] == 0 

def getAround(i,j,m,n):
	res = []
	for k in [1]:
		if isLegal(i+k,j,m,n):
			res.append((i+k,j))
		if isLegal(i,j+k,m,n):
			res.append((i,j+k))
	return res
count = 0
def find(i,j,m,n):
	if (i,j) == (m-1,n-1):
		print(np.array(obstacleGrid))
		global count
		count += 1
		return
	aroundArr = getAround(i,j,m,n)
	for loc in aroundArr:
		next_i = loc[0]
		next_j = loc[1]
		obstacleGrid[next_i][next_j] = 2
		find(next_i,next_j,m,n)
		obstacleGrid[next_i][next_j] = 0

m = len(obstacleGrid)
n = len(obstacleGrid[0])
obstacleGrid[0][0] = 2
find(0,0,m,n)
print(count)
	

>>>>>>> bae8e88720199da471e2e3355c6162ce9f33451f
