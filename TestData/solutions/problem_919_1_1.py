class Solution:
    def solution_919_1_1(self, root: TreeNode) -> TreeNode:
        
        def solution_919_1_2(node):
            """inorder depth-first traverse bst"""
            if not node: return 
            solution_919_1_2(node.left)
            value.append(node.val)
            solution_919_1_2(node.right)
        
        value = [] #collect values
        solution_919_1_2(root)
        
        def solution_919_1_3(lo, hi): 
            if lo > hi: return None
            mid = (lo + hi)//2
            ans = TreeNode(value[mid])
            ans.left = solution_919_1_3(lo, mid-1)
            ans.right = solution_919_1_3(mid+1, hi)
            return ans
        
        return solution_919_1_3(0, len(value)-1)