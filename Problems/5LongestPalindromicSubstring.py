class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_len = 0
        res = s[0]
        for i in range(n):
            odd = min(i,n-i-1)
            for step in range(0,odd+1):
                A = i + step
                B = i - step
                if s[A] == s[B]:
                    if max_len < 2*step + 1:
                        max_len = 2*step + 1
                        res = s[B:A+1]
                else:
                    break
            even = min(i,n-2-i)
            for step in range(0,even+1):
                A = i+1+step
                B = i - step
                if s[A] == s[B]:
                    if max_len < 2*step + 2:
                        max_len = 2*step + 2
                        res = s[B:A+1]
                else:
                    break
        return res