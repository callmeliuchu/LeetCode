class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.f(candidates,target,[],ans)
        return ans
        
    def f(self,arr,target,res,ans):
        if target < 0:
            return
        if target == 0:
            new_arr = sorted(res)
            if new_arr not in ans:
                ans.append(new_arr)
        for val in arr:
            res.append(val)
            self.f(arr,target-val,res,ans)
            res.pop()