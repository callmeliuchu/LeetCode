class Solution:
    def swap(self,arr,i,j):
        arr[i],arr[j] = arr[j],arr[i]
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.f(nums,0,res)
        return res
        
    def f(self,arr,index,res):
        if index == len(arr):
            res.append(arr[:])
        for i in range(index,len(arr)):
            self.swap(arr,i,index)
            self.f(arr,index+1,res)
            self.swap(arr,i,index) 