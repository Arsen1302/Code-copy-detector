class Solution(object):
    def solution_502_1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        _l = self.solution_502_1(root.left)
        _r = self.solution_502_1(root.right)
        if root.val == 0 and _l == None and _r == None:
            return None
        else:
            root.left = _l
            root.right = _r
        return root