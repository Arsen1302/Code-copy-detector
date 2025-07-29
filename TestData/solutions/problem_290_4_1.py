class Solution:
    def solution_290_4_1(self, root: Optional[TreeNode]) -> List[int]:
        
        modes = {}
        
        def solution_290_4_2(node):
            if not node: return node
            
            modes[node.val] = modes.get(node.val, 0) + 1
            
            solution_290_4_2(node.left)
            solution_290_4_2(node.right)
        
        solution_290_4_2(root)
        
        result = []
        max_value = max(modes.values())
        for k, v in modes.items():
            if v == max_value:
                result.append(k)
        return result