class Solution:
    def solution_170_4_1(self):
        self.cache = {}
		
    def solution_170_4_2(self, root: TreeNode) -> int:
        return max(self.solution_170_4_3(root, 0), self.solution_170_4_3(root, 1))
    
    def solution_170_4_3(self, root, status): # status == 0 means skip
        if not root:
            return 0
        if (root,status) in self.cache:
            return self.cache[(root, status)]
        if status == 1:
            res = root.val + self.solution_170_4_3(root.left, 0) + self.solution_170_4_3(root.right, 0)
        else:
            res = max(self.solution_170_4_3(root.left,0), self.solution_170_4_3(root.left,1)) + max(self.solution_170_4_3(root.right,0), self.solution_170_4_3(root.right,1))
        self.cache[(root, status)] = res
        return res