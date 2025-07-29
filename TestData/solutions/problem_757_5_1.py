class Solution:
    def solution_757_5_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        DFS, check the height of left and right
        
        if left==right, the node itself is the LCA
        if left>right, the LCA stays in the left side
        if left <right, the LCA stays in the right side
        
        '''
        
        return self.solution_757_5_2(root,0)[0]
        
    def solution_757_5_2(self, root, height):
        if root is None:
            return (None,0)
        left=self.solution_757_5_2(root.left, height)
        right=self.solution_757_5_2(root.right,height)
        
        if left[1]==right[1]:
            return (root,left[1]+1)

        if left[1]>right[1]:
            return (left[0],left[1]+1)
        
        if left[1]<right[1]:
            return (right[0],right[1]+1)