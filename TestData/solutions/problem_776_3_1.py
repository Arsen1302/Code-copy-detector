class Solution:
    def solution_776_3_1(self, root: Optional[TreeNode]) -> int:
        levels = []
        sums = float('-inf')
        res = 0
        
        def solution_776_3_2(node, level):
            if level >= len(levels):
                levels.append([])
            
            if node:
                levels[level].append(node.val)
                if node.left:
                    solution_776_3_2(node.left, level + 1)
                    
                if node.right:
                    solution_776_3_2(node.right, level + 1)
        
        solution_776_3_2(root, 0)
        
        for i in range(len(levels)):
            if sum(levels[i]) > sums:
                sums = sum(levels[i])
                res = i + 1
                
        return res