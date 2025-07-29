class Solution:
    def solution_58_3(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        postorder, stack = [], [root]
        while stack:
            node = stack.pop()
            if not node: 
                continue
            postorder.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return postorder[::-1]