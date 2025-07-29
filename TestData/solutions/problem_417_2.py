class Solution:
    def solution_417_2(self, root, val):
        if not root:
            return TreeNode(val)
      
        if val<root.val:
            root.left = self.solution_417_2(root.left, val)
        else:
            root.right = self.solution_417_2(root.right, val)
  
        return root