class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        for i in range(len(nums)+1):
            self.dfs(nums,0,i,[])
        return self.res

    def dfs(self,nums,index,k,tmp_arr):
        if len(tmp_arr) == k:
            # print(tmp_arr)
            self.res.append(tmp_arr[:])
            return
        for i in range(index,len(nums)):
            tmp_arr.append(nums[i])
            self.dfs(nums,i+1,k,tmp_arr)
            tmp_arr.pop()