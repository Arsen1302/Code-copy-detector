class Solution:
    def solution_298_4(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        ii = -1
        while stack:
            node, i = stack.pop()
            if i > ii: ans, ii = node.val, i # left-most node val 
            if node.right: stack.append((node.right, i+1))
            if node.left: stack.append((node.left, i+1))
        return ans