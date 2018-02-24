class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return self.multi(num1,num2)
    def reverseMulti(self,arr1,arr2):
        arr_len = len(arr1) + len(arr2)
        arr = [0]*arr_len
        for j in range(len(arr2)):
            for i in range(len(arr1)):
                num = arr2[j]*arr1[i]
                arr[j+i] += num
                arr[j+i+1] += arr[j+i]//10
                arr[j+i] = arr[j+i]%10
        for j in range(len(arr)-1):
            arr[j+1] += arr[j]//10
            arr[j] = arr[j]%10
        return arr

    def reverse(self,arr):
        return [arr[i] for i in range(len(arr)-1,-1,-1)]

    def multiByArr(self,arr1,arr2):
        arr_1 = self.reverse(arr1)
        arr_2 = self.reverse(arr2)
        arr = self.reverseMulti(arr_1,arr_2)
        res = ''
        flag = False
        for i in range(len(arr)-1,-1,-1):
            if arr[i] != 0:
                flag = True
            if flag:
                res = res + str(arr[i])
        if len(res) == 0:
            return '0'
        return res


    def strToNumArr(self,str1):
        return [int(num) for num in str1]


    def multi(self,str1,str2):
        num1 = self.strToNumArr(str1)
        num2 = self.strToNumArr(str2)
        return self.multiByArr(num1,num2)