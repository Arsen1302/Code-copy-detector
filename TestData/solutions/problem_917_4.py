class Solution:
    def solution_917_4(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack: 
            x, y = stack.pop()
            if x == target: return y
            if x:
                stack.append((x.left, y.left))
                stack.append((x.right, y.right))