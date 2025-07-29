class Solution:
    def solution_917_5(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return cloned
        if cloned.val == target.val:
            return cloned
        a = self.solution_917_5(original, cloned.left, target)
        if a is not None:
            return a
        else:
            return self.solution_917_5(original, cloned.right, target)