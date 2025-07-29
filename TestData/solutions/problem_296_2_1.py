class Solution:
    def solution_296_2_1(self, root: TreeNode) -> List[int]:
        
        def solution_296_2_2(node):
            """Populate frequency table."""
            if not node: return 0 
            ans = node.val + solution_296_2_2(node.left) + solution_296_2_2(node.right)
            freq[ans] = 1 + freq.get(ans, 0)
            return ans 
        
        freq = {}
        solution_296_2_2(root)
        most = max(freq.values(), default=0)
        return [k for k, v in freq.items() if v == most]