class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.getIndexArr(nums,target)
    def mid(self,arr,target):
        start = 0
        end = len(arr)-1
        while start <= end:
            mid = (start + end)//2
            if arr[mid] < target:
                start = mid+1
            elif arr[mid] > target:
                end = mid-1
            else:
                return mid
        return -1

    def  getIndexArr(self,arr,target):
        loc = self.mid(arr,target)
        if loc == -1:
            return [-1,-1]
        start_index = loc
        while start_index>=0 and arr[start_index]==target:
            start_index = start_index - 1
        end_index = loc
        while end_index<len(arr) and arr[end_index]==target:
            end_index = end_index + 1
        return [start_index+1,end_index-1]