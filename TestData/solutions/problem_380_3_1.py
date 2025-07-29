class Solution:
    def solution_380_3_1(self, root: TreeNode, k: int) -> bool:
        def solution_380_3_2(node: TreeNode, numbers):
            if node:
                if k - node.val in numbers: return True 
                numbers.add(node.val)
                return solution_380_3_2(node.right, numbers) or solution_380_3_2(node.left, numbers)
            
        return solution_380_3_2(root, set())