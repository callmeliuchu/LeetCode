class Solution:
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if n == 1:
            return s
        total = len(s)
        columns = total//(2*n-2)
        print(total,columns)
        res = ''
        for i in range(n):
            for step in range(columns+1):
                index_1 = i + step*(2*n-2)
                if index_1 < total:
                    res = res + s[index_1]
                if i!=0 and i!=n-1:
                    index_2 = (2*n-2) - i  + (2*n-2)*step
                    if index_2 < total:
                        res = res + s[index_2]
        return res