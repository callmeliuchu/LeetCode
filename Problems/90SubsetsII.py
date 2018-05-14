class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        self.res = []
        for i in range(len(nums)+1):
            self.dfs(nums,0,i,[])
        return self.res

    def dfs(self,nums,index,k,tmp_arr):
        if len(tmp_arr) == k and tmp_arr not in self.res:
            # print(tmp_arr)
            self.res.append(tmp_arr[:])
            return
        for i in range(index,len(nums)):
            tmp_arr.append(nums[i])
            self.dfs(nums,i+1,k,tmp_arr)
            tmp_arr.pop()