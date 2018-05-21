class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m1 = self.count(s)
        m2 = self.count(t)
        for key in m2:
            if key not in m1:
                return key
            if m1[key] != m2[key]:
                return key
    
    def count(self,s):
        res = {}
        for c in s:
            if c in res:
                res[c] += 1
            else:
                res[c] = 1
        return res