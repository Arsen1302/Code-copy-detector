class Solution:
    def solution_552_4_1(self, root: TreeNode) -> TreeNode:
        
        max_depth, max_depth_subtree = self.solution_552_4_2(root, 0) 
        
        return max_depth_subtree
        
    
    def solution_552_4_2(self, root, depth): 
        if not root: 
            return depth, root
        
        left_max_depth, left_max_depth_subtree = self.solution_552_4_2(root.left, depth + 1) 
        right_max_depth, right_max_depth_subtree = self.solution_552_4_2(root.right, depth + 1) 
        
		## if max depth of left subtree equals to max depth of right subtree, root is the LCA
        if left_max_depth == right_max_depth:  
            return left_max_depth, root
			
        ## if left subtree is deeper, return left subtree 
        if left_max_depth > right_max_depth: 
            return left_max_depth, left_max_depth_subtree 
        
        ## if right subtree is deeper, return right subtree
        return right_max_depth, right_max_depth_subtree