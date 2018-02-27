class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.genP('',n,n,res)
        return res
        
    def genP(self,s,left,right,res):
        if left > right:
            return
        if left > 0:
            self.genP(s+'(',left-1,right,res)
        if right > 0:
            self.genP(s+')',left,right-1,res)
        if left == 0 and right == 0:
            res.append(s)