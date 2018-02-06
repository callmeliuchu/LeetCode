class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        max_len = 0
        for i in range(length):
            tmp = s[i]
            for j in range(i+1,length):
                if s[j] not in tmp:
                    tmp = tmp + s[j]
                else:
                    break
            if max_len < len(tmp):
                max_len = len(tmp)
        return max_len