class Solution:
    def solution_394_3_1(self, root: Optional[TreeNode]) -> int:
        
        
        v = []
        def solution_394_3_2(tree):
            
            if not tree:
                return
            
            v.append(tree.val)
            solution_394_3_2(tree.left)
            solution_394_3_2(tree.right)
        
        solution_394_3_2(root)
        
        nodes = []
        for node in v:
            if node not in nodes:
                nodes.append(node)
        
        if len(nodes) == 1:
            return -1
        
        return sorted(nodes)[1]