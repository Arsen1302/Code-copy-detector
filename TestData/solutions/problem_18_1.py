class Solution:
    def solution_18_1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        loc = {x : i for i, x in enumerate(inorder)}
        root = None
        stack = []
        for x in preorder: 
            if not root: root = node = TreeNode(x)
            elif loc[x] < loc[node.val]: 
                stack.append(node)
                node.left = node = TreeNode(x)
            else: 
                while stack and loc[stack[-1].val] < loc[x]: node = stack.pop() # backtracking
                node.right = node = TreeNode(x)
        return root