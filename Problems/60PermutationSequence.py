class Solution:
    def getPermutation(self, n, k):
        arr = list(range(1,n+1))
        size = len(arr)
        k = k - 1
        ret_val = 0
        for i in range(size,0,-1):
            t = self.f(i-1)
            index =  k//t
            val = arr[index]
            ret_val = ret_val*10 + val
            del arr[index]
            k = k - index*t
        return str(ret_val)
    
    def f(self,n):
        if n == 0:
            return 1
        return n*self.f(n-1)