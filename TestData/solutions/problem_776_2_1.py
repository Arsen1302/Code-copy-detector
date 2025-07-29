class Solution:
    def solution_776_2_1(self, root: Optional[TreeNode]) -> int:
        def solution_776_2_2(node, level):
            if not node:
                return
            
            sums[level] += node.val                
            solution_776_2_2(node.left, level + 1)
            solution_776_2_2(node.right, level +1 )
        
        sums = defaultdict(int)
        solution_776_2_2(root, 1)
        
        result = 1
        max_sum = sums[1]
        for level, s in sums.items():
            if s > max_sum:
                max_sum = s
                result = level
        
        return result