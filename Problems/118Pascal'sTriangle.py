class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            vec = [0]*(i+1)
            vec[0] = 1
            vec[-1] = 1
            for j in range(1,i):
                vec[j] = res[i-1][j-1] + res[i-1][j]
            res.append(vec)
        return res