class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        res = []
        for i in range(size):
            tmp = []
            for j in range(size-1,-1,-1):
                tmp.append(matrix[j][i])
            res.append(tmp)
        for i in range(size):
            for j in range(size):
                matrix[i][j] = res[i][j]