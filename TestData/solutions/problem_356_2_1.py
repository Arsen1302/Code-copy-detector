class Solution:
    def solution_356_2_1(self, t: TreeNode) -> str:
        sb = [] # init string builder
        
        # solution_356_2_2 function to create result
        def solution_356_2_2(node: TreeNode) -> None:
            if not node:
                return
            
            sb.append('(')                      # add 1st wrapping parenthesis
            sb.append(str(node.val))
            
            solution_356_2_2(node.left)                   # process left recursively
            
            if not node.left and node.right:    # add parenthesis if left is empty but right exists
                sb.append('()')
                
            solution_356_2_2(node.right)                  # process right recursively
            
            sb.append(')')                      # add 2nd wrapping parenthesis
        
        solution_356_2_2(t)

        # trim 1st and last parenthesis build result string
        return ''.join(sb[1:-1])