class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.isSame = True
        self.judge(p,q)
        self.judge(q,p)
        return self.isSame
    
    def judge(self,p,q):
        if p:
            if not q:
                self.isSame = False
                return
            else:
                if p.val != q.val:
                    self.isSame = False
                    return
            self.judge(p.left,q.left)
            if not q:
                self.isSame = False
                return
            else:
                if p.val != q.val:
                    self.isSame = False
                    return
            self.judge(p.right,q.right)