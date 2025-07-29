class Solution:
    def solution_359_1(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1: return root2
        if not root2: return root1
        queue = deque([(root1, root2)])
        while queue:
            current_root1, current_root2 = queue.pop()
            if current_root1.left and current_root2.left: queue.append((current_root1.left, current_root2.left))
            elif not current_root1.left: current_root1.left = current_root2.left
            if current_root1.right and current_root2.right: queue.append((current_root1.right, current_root2.right))
            elif not current_root1.right: current_root1.right = current_root2.right
            current_root1.val += current_root2.val
        return root1