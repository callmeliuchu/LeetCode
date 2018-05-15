class Solution(object):
    def restoreIpAddresses(self, s):
        if len(s) > 12:
            return []
        return self.get_ips(s)
        
    def get_ips(self,ip):
        ip_len = len(ip) - 1
        ips = []
        res = []
        self.find_k_from_n(ip_len,3,0,[],res)
        for vec in res:
            tmp_ip = self.get_ip(ip,vec)
            if tmp_ip:
                ips.append(tmp_ip)
        return ips

    def get_ip(self,ip,vec):
        num_len = len(ip)
        vec.append(num_len)
        res = []
        s = 0
        for index in vec:
            e = index+1
            tmp_slice = ip[s:e]
            if not self.isLegal(tmp_slice):
                return None
            res.append(tmp_slice)
            s = e
        return '.'.join(res)
    
    def isLegal(self,tmp_slice):
        if int(tmp_slice) > 255:
            return False
        if len(tmp_slice) > 1 and tmp_slice[0] == '0':
            return False
        return True
        


    def find_k_from_n(self,n,k,index,tmp_arr,res):
        if len(tmp_arr) == k:
            res.append(tmp_arr[:])
            return
        for i in range(index,n):
            tmp_arr.append(i)
            self.find_k_from_n(n,k,i+1,tmp_arr,res)
            tmp_arr.pop()