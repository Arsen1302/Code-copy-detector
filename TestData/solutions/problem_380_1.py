class Solution:
    def solution_380_1(self, root: TreeNode, k: int) -> bool:
        queue = [root]
        unique_set = set()
        
        while len(queue) > 0:
            current = queue.pop()
            if k - current.val in unique_set: return True
            unique_set.add(current.val)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        
        return False