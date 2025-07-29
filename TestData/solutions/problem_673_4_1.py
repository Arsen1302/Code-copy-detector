class Solution:
    def solution_673_4_1(self, root: TreeNode, x: int, y: int) -> bool:
        
        def solution_673_4_2(node, k, parent): 
            """Traverse the subtree rooted at node"""
            if node is None: return 
            if node.val in (x, y): ans[node.val] = (k, parent)
            solution_673_4_2(node.left, k+1, node)
            solution_673_4_2(node.right, k+1, node)
        
        ans = dict()
        solution_673_4_2(root, 0, None)
        return ans[x][0] == ans[y][0] and ans[x][1] != ans[y][1]