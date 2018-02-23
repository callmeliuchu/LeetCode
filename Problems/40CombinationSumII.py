class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.f(sorted(candidates),0,target,[])
        return self.res
        
    def f(self,arr,index,target,tmp):
        if target < 0:
            return
        if target == 0:
            if tmp not in self.res:
                self.res.append(tmp[:])
        for i in range(index,len(arr)):
            tmp.append(arr[i])
            self.f(arr,i+1,target-arr[i],tmp)
            tmp.pop()