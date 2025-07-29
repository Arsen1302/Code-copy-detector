class Solution:
    def solution_619_4_1(self, root: TreeNode, low: int, high: int) -> int:
        
        result = []
        self.solution_619_4_2(root, low, high, result)
        return sum(result)
        
        
    def solution_619_4_2(self, root, low, high, result):
        if root:
            if root.val < low:
                self.solution_619_4_2(root.right, low, high, result)
                
            if root.val > high:
                self.solution_619_4_2(root.left, low, high, result)
                
            if low <= root.val <= high:
                result.append(root.val)
                self.solution_619_4_2(root.left, low, high, result)
                self.solution_619_4_2(root.right, low, high, result)