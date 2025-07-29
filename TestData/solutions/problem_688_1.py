class Solution:
    def solution_688_1(self, preorder: List[int]) -> TreeNode:
        node_stack = []
        node = root = TreeNode(preorder[0])
        for n in preorder[1:]:
            if n <= node.val:
                node.left = TreeNode(n)
                node_stack.append(node)
                node = node.left
            else:
                while node_stack and n > node_stack[-1].val:
                    node = node_stack.pop()
                node.right = TreeNode(n)
                node = node.right
        return root