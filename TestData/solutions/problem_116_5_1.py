class Solution:
    def solution_116_5_1(self, root: TreeNode, result:list) -> None:
        if root:
            self.solution_116_5_1(root.left, result)
            result.append(root.val)
            self.solution_116_5_1(root.right, result)
            
    def solution_116_5_2(self, root: Optional[TreeNode], k: int) -> int:
        if root:
            result = []
            self.solution_116_5_1(root, result)
            return result[k-1]