class Solution:
    def solution_583_1_1(self, root: TreeNode) -> TreeNode:
        
        prev_node = None
        
        def solution_583_1_2( node: TreeNode):
                           
            if node.right:
                solution_583_1_2( node.right )

            # prev_novde always points to next larger element for current node
            nonlocal prev_node

            # update right link points to next larger element
            node.right = prev_node

            # break the left link of next larger element
            if prev_node:
                prev_node.left = None

            # update previous node as current node
            prev_node = node

            if node.left:
                solution_583_1_2( node.left)
                
        # ---------------------------------------
        solution_583_1_2( root )
        
        return prev_node