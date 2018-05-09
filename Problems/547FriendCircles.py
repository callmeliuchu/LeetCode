class Solution:
    def findCircleNum(self, graph):
        m = len(graph)
        data_arr = [-1]*m
        for i in range(m):
            for j in range(0,i):
                if graph[i][j] == 1:
                    self.unit(data_arr,i,j)
        res = 0
        for val in data_arr:
            if val < 0:
                res += 1
        return res
        
    def get_root(self,data_arr,i):
        while data_arr[i]>=0:
            i = data_arr[i]
        return i


    def unit(self,data_arr,i,j):
        root1 = self.get_root(data_arr,i)
        root2 = self.get_root(data_arr,j)
        val1 = data_arr[root1]
        val2 = data_arr[root2]
        if data_arr[root1] > data_arr[root2]:
            data_arr[root1] = root2
            data_arr[root2] = val1 + val2
        else:
            data_arr[root2] = root1
            data_arr[root1] = val1 + val2