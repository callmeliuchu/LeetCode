import re
t = re.match('\d+?.\d+?','1')
print(t)

# class Solution:
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         self.res = []
#         self.getRes(sorted(nums),0,0,[],target)
#         return self.res
        
#     def getRes(self,nums,index,count,tmp,target):
#         if count == 4 and sum(tmp) == target:
#             if tmp not in self.res:
#                 self.res.append(tmp[:])
#             return
#         for i in range(index,len(nums)):
#             tmp.append(nums[i])
#             self.getRes(nums,i+1,count+1,tmp,target)
#             tmp.pop()
