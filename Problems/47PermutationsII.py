class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.f(nums,0)
        return self.res
        
    def swap(self,arr,i,j):
        arr[i],arr[j] = arr[j],arr[i]


    def f(self,arr,index):
        if index == len(arr):
            if arr not in self.res:
                self.res.append(arr[:])
        for i in range(index,len(arr)):
            self.swap(arr,i,index)
            self.f(arr,index+1)
            self.swap(arr,i,index)