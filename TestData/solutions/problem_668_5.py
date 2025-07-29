class Solution:
    def solution_668_5(self, root: TreeNode) -> str:
        ans = ""
        stack = [(root, "")]
        while stack: 
            node, ss = stack.pop()
            ss += chr(node.val + 97)
            if node.left is node.right: 
                ans = min(ans, ss[::-1]) if ans else ss[::-1]
            else: 
                if node.left: stack.append((node.left, ss))
                if node.right: stack.append((node.right, ss))
        return ans