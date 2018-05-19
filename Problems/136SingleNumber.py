class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for val in nums:
            if val in counter:
                counter[val] += 1
            else:
                counter[val] = 1
        for key in counter:
            if counter[key] == 1:
                return key