class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        total = m*n
        a = 0
        b = 0
        c = a + m -1
        d  =b + n - 1
        res = []
        count = 0
        while a <= c and b <= d:
            for i in range(b,d+1):
                if count < total:
                    res.append(matrix[a][i])
                    count += 1
            for i in range(a+1,c+1):
                if count < total:
                    res.append(matrix[i][d])
                    count += 1
            for i in range(d-1,b-1,-1):
                if count < total:
                    res.append(matrix[c][i])
                    count += 1
            for i in range(c-1,a,-1):
                if count < total:
                    res.append(matrix[i][b])
                    count += 1
            a += 1
            b += 1
            c -= 1
            d -= 1
        return res