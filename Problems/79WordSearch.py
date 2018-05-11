class Solution:
    def exist(self,board,word):
        index = 0
        arr = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[index]:
                    arr.append((i,j))
        index += 1
        for i,j in arr:
            visited = []
            visited.append((i,j))
            if self.find(board,word,i,j,index,visited):
                return True
        return False

    def is_legal(self,board,i,j):
        m = len(board)
        n = len(board[0])
        return i >= 0 and i<m and j>=0 and j<n


    def get_arround(self,board,i,j,char,visited):
        ret_arr = []
        for k in [-1,1]:
            if  self.is_legal(board,i,j+k) and (i,j+k) not in visited and board[i][j+k] == char:
                ret_arr.append((i,j+k))
            if  self.is_legal(board,i+k,j) and (i+k,j) not in visited and board[i+k][j] == char:
                ret_arr.append((i+k,j))
        return ret_arr


    def find(self,board,word,i,j,word_index,visited):
        if len(word) == word_index:
            return True
        around_arr = self.get_arround(board,i,j,word[word_index],visited)
        if len(around_arr) == 0:
            return False
        for i1,j1 in around_arr:
            visited.append((i1,j1))
            if self.find(board,word,i1,j1,word_index+1,visited):
                return True
            visited.pop()
        return False