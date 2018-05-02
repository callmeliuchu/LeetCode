class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.f(haystack, needle)
    def f(self,haystack,needle):
        ha_size = len(haystack)
        ne_size = len(needle)
        if ha_size == 0 and ne_size == 0:
            return 0
        for i in range(ha_size):
            tmp = haystack[i:i+ne_size]
            if tmp == needle:
                return i
        return -1