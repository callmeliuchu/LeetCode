class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dataSet = {}
        for c in s:
            if c in dataSet:
                dataSet[c] += 1
            else:
                dataSet[c] = 1
        arr = sorted(dataSet.items(),key=lambda x:x[1],reverse=True)
        new_arr = [item[0]*item[1] for item in arr]
        return ''.join(new_arr)