# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false. 
import  random
def canJump(nums):
	queue = []
	queue.append(0)
	while len(queue) > 0:
		index = queue.pop(0)
		if nums[index] + index >= len(nums) - 1:
			return True
		for i in range(index+1,index+nums[index]+1):
			queue.append(i)
	return False

# print(canJump([2,3,1,1,4]))

# print(canJump([3,2,1,0,4]))

def getRandNums(n):
	s = ''
	for i in range(n):
		s += str(int(10*random.random()))
	return s

res = getRandNums(18)
print(res)