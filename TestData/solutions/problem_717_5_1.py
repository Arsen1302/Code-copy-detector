class Solution:
    def solution_717_5_1(self):
        self.greaterSum = 0

    def solution_717_5_2(self, root: TreeNode) -> TreeNode:
        return self.solution_717_5_3(root)
    
    def solution_717_5_3(self, root):
        if (not root): return
        
        # compute greater sum using the right subtree from a reverse(right-middlee-left) in-order traversal order
        self.solution_717_5_3(root.right)
        self.greaterSum += root.val
        root.val = self.greaterSum
        self.solution_717_5_3(root.left)
        
        return root