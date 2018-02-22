class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        count = {}
        for val in strs:
            key = self.toKey(val)
            if key not in count:
                count[key] = []
            count[key].append(val)
        res = []
        for _,val in count.items():
            res.append(val)
        return res
            
            
    
    def toKey(self,aStr):
        return ''.join(sorted(aStr))