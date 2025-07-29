class Solution:
    def solution_639_5(self, root: TreeNode) -> bool:
        queue = [root]
        while queue[0]:
            node = queue[0]
            queue = queue[1:]
            queue.append(node.left)
            queue.append(node.right)
        return not any(queue)