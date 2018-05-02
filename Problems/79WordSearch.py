board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = 'SEEHHHH'

arr = [1,2]
val = arr.pop(0)

def find(board,word):
	queue = []
	index = 0
	m = len(board)
	n = len(board[0])
	visited = set()
	for i in range(m):
		for j in range(n):
			if board[i][j] == word[index]:
				if (i,j) not in visited:
					queue.append((i,j))
					visited.add((i,j))
	while len(queue)>0:
		i,j = queue.pop(0)
		index += 1
		if index == len(word):
			break
		char = word[index]
		search(queue,visited,board,i,j,char)
	return index == len(word)

def search(queue,visited,board,i,j,char):
	m = len(board)
	n = len(board[0])
	for k in [-1,1]:
		if i+k>=0 and i+k<m:
			if board[i+k][j] == char:
				if (i+k,j) not in visited:
					queue.append((i+k,j))
					visited.add((i+k,j))
		if j+k>=0 and j+k<n:
			if board[i][j+k] == char:
				if (i,j+k) not in visited:
					queue.append((i,j+k))
					visited.add((i,j+k))

isTrue = find(board,word)
print(isTrue)

