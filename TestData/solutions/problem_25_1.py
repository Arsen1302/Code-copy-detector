class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def solution_25_1(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return target == root.val
        return self.solution_25_1( root.left, target - root.val) or \
               self.solution_25_1(root.right, target - root.val)