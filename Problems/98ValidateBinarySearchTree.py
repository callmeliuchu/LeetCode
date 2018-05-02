class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True
        self.isValid = True
        self.judge(root)
        return self.isValid
    
    def judge(self,root):
        if root:
            self.judge(root.left)
            if self.flag :
                self.flag = False
                self.num = root.val
            else:
                if root.val<=self.num:
                    self.isValid = False
                    return
                else:
                    self.num = root.val
            self.judge(root.right)