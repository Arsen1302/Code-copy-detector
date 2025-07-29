class Solution:
    def solution_917_3(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if original is None:
            return 
        elif original == target:
            return cloned
        else:
            return self.solution_917_3(original.left, cloned.left, target) or self.solution_917_3(original.right, cloned.right, target)