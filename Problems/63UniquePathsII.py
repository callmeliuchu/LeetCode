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
	

