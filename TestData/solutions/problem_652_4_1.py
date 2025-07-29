class Solution:
    def solution_652_4_1(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        def solution_652_4_2(node, i): 
            """Return if tree can be flipped to match traversal &amp; size."""
            if not node: return True, 0 
            if node.right and node.right.val == voyage[i+1]: 
                if node.left: 
                    ans.append(node.val)
                    node.left, node.right = node.right, node.left 
            ltf, lx = solution_652_4_2(node.left, i+1)
            rtf, rx = solution_652_4_2(node.right, i+1+lx)
            return node.val == voyage[i] and ltf and rtf, 1 + lx + rx
        
        ans = []
        return ans if solution_652_4_2(root, 0)[0] else [-1]