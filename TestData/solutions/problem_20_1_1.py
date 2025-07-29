class Solution:
    def solution_20_1_1(self, result, depth, node):
        if not node:
            return
        
        if len(result) < depth:
            result.append([])
            
        result[depth-1].append(node.val)
        self.solution_20_1_1(result, depth+1, node.left)
        self.solution_20_1_1(result, depth+1, node.right)
        
    def solution_20_1_2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        depth = 1
        self.solution_20_1_1(result, depth, root)
        result.reverse()
        return result