class Solution:
    def solution_356_1_1(self, t: TreeNode) -> str:
        sb = [] # init string builder
        
        # solution_356_1_2 function to create result
        def solution_356_1_2(node: TreeNode) -> None: 
            if not node:
                return
            
            sb.append(str(node.val))
            
            if not node.left and not node.right:
                # leaf node, stop processing
                return
            
            sb.append('(')          # always wrap left node with parenthesis when right node exist
            solution_356_1_2(node.left)       # process left node recursively 
            sb.append(')')                         

            if node.right:          # adding parenthesis for the right node only if it is not empty
                sb.append('(')
                solution_356_1_2(node.right)
                sb.append(')') 
        
        solution_356_1_2(t)

        return ''.join(sb)