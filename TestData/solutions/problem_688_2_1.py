class Solution:
    def solution_688_2_1(self, preorder: List[int]) -> TreeNode:
        
        root_index = 0
        
        def solution_688_2_2( preorder, upperbound):
            
            nonlocal root_index
            
            if root_index == len(preorder) or preorder[root_index] > upperbound:
                return None
            
            root = TreeNode( preorder[root_index] )
            
            # update root index by adding one
            root_index += 1
            
            root.left = solution_688_2_2( preorder, root.val )
            root.right = solution_688_2_2( preorder, upperbound )

            return root
                
        return solution_688_2_2( preorder, float('inf') )