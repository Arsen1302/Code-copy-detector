class Solution:
    def solution_911_2_1(self, root: Optional[TreeNode]) -> int:
        
        # initialize a instance variable in order to
        # save the maximum path length
        self.max_path = 0
        
        # make the DFS
        self.solution_911_2_2(root, -1, 0)
        
        # return path length
        return self.max_path
    
    def solution_911_2_2(self, node, prev_direction, path_length):
        # end condition for solution_911_2_2
        if node is None:
            return
        
        # add current length to max path
        # print(path_length)
        self.max_path = max(path_length, self.max_path)
        
        if prev_direction == 1:
            self.solution_911_2_2(node.left, 1, 1)
            self.solution_911_2_2(node.right, 2, path_length+1)
        else:
            self.solution_911_2_2(node.left, 1, path_length+1)
            self.solution_911_2_2(node.right, 2, 1)