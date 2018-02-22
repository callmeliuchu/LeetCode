class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if n < 0:
            x = 1/x
            n = -n
        return self.pow(x,n)
    
    def pow(self,x,n):
        if n == 0:
            return 1
        if n % 2 == 1:
            return x*self.pow(x,n-1)
        else:
            return self.pow(x,n/2)**2