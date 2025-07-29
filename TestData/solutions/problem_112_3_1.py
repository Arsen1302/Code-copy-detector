class Solution:
    
    def solution_112_3_1(self,root):
        if (root==None) or (root.left==None and root.right==None):
            return root
        temp = root.right
        root.right = self.solution_112_3_1(root.left)
        root.left = self.solution_112_3_1(temp)
        return root

    def solution_112_3_2(self, root: TreeNode) -> TreeNode:
        return self.solution_112_3_1(root)