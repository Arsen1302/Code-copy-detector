class Solution:
    def solution_473_3_1(self):
        self.arr = []
    def solution_473_3_2(self,node):
        if node is None:
            return []
        if node:
            self.solution_473_3_2(node.left)
            self.arr.append(node.val)
            self.solution_473_3_2(node.right)
        return self.arr
        
            
    def solution_473_3_3(self, root: Optional[TreeNode]) -> int:
        inorder = self.solution_473_3_2(root)
        min_diff = float("inf")
        for i in range(1,len(inorder)):
            min_diff = min(min_diff,abs(inorder[i]-inorder[i-1]))
        return min_diff