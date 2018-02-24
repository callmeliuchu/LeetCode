class Solution:
    def jump(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        currentMax = 0
        level = 0
        nextMax = 0
        while True:
            for i in range(index,currentMax+1):
                index = index + 1
                nextMax = max(nextMax,arr[i]+i)
                if currentMax >= len(arr)-1:return level
            currentMax = nextMax
            level = level + 1
        return level