class Solution:
    def solution_619_2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        res = root.val if low <= root.val <= high else 0
        if root.val <= low: return res + self.solution_619_2(root.right, low, high)
        if root.val >= high: return res + self.solution_619_2(root.left, low, high)
        return res + self.solution_619_2(root.right, low, high) + self.solution_619_2(root.left, low, high)