class Solution:
    def solution_380_4_1(self, root: Optional[TreeNode], k: int) -> bool:
        def solution_380_4_2(node, seen):
            if not node:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)            
            return solution_380_4_2(node.left, seen) or solution_380_4_2(node.right, seen)
        
        return solution_380_4_2(root, set())