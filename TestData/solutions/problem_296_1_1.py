class Solution:
    def solution_296_1_1(self, root: TreeNode) -> List[int]:
        
        counts = collections.Counter()
        
        def solution_296_1_2(node):
            if not node: return 0            
            result = node.val + solution_296_1_2(node.left) + solution_296_1_2(node.right)
            counts[result] += 1        
            return result
        
        solution_296_1_2(root)       
        
        # Try to return the most frequent elements
        # Return [] if we run into index errors
        try:
            freq = counts.most_common(1)[0][1]
            return [x[0] for x in counts.items() if x[1] == freq]
        except:
            return []