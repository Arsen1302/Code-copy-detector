class Solution:
    def solution_738_2_1(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def solution_738_2_2(node, pathSum):
            #For non-leaf nodes return invalid path sum
            if(node is None):   return limit - 1, None
            
            pathSumWithCurrentNode = pathSum + node.val
            
            #For leaf node return the path sum
            if(node.left is None and node.right is None):
                leftPathSum = rightPathSum = pathSumWithCurrentNode
            else:
                leftPathSum, node.left = solution_738_2_2(node.left, pathSumWithCurrentNode)
                rightPathSum, node.right = solution_738_2_2(node.right, pathSumWithCurrentNode)
                
            if(leftPathSum >= limit or rightPathSum >= limit):
                #including the current node
                return max(leftPathSum, rightPathSum), node
            
            #Removing the current node
            return min(leftPathSum, rightPathSum), None
        
        _, newRoot = solution_738_2_2(root, 0)
        return newRoot