nums = [4, 3, 2, 3, 5, 2, 1]
k = 4

def canPartitionKSubsets(nums, k):
	sum_nums = sum(nums)
	if sum_nums % k !=0:
		return False

def f(nums,k,visited):
	

canPartitionKSubsets(nums,k) 