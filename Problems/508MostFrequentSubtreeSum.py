class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dataSet = {}
        self.dfs(root,0)
        counter = {}
        for _,value in self.dataSet.items():
            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1
        max_val = 0
        for key,value in counter.items():
            if max_val < value:
                max_val = value
        ret_arr = []
        for key,value in counter.items():
            if max_val == value:
                ret_arr.append(key)       
        return ret_arr
        
                
            
    
    def dfs(self,root,index):
        if root:
            self.dfs(root.left,index*2+1)
            self.dfs(root.right,index*2+2)
            if index*2+1 in self.dataSet:
                a = self.dataSet[index*2+1]
            else:
                a = 0
            if index*2+2 in self.dataSet:
                b = self.dataSet[index*2+2]
            else:
                b = 0
            self.dataSet[index] = a + b + root.val