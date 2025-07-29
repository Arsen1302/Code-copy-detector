class Solution:
    
    def solution_1512_5_1(self, descriptions):
        g = {}
        in_degree = {}
        
        for parent, child, is_left in descriptions:
            if parent not in g: 
                g[parent] = [None, None]
            if child not in g:
                g[child] = [None, None]
            
            if parent not in in_degree: in_degree[parent] = 0
            if child not in in_degree: in_degree[child] = 0
            
            in_degree[child] += 1
            # if is_left is true will be in 1st pos, else it will be inserted in right child
            g[parent][is_left] = child
        
        return [g, in_degree]
    
    def solution_1512_5_2(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        g, in_degree = self.solution_1512_5_1(descriptions)
        root = None
        for vertex, in_deg in in_degree.items():
            if in_deg == 0:
                root = vertex
                break
        
        root_node = TreeNode(root)
        q = deque([root_node])
        while q:
            curr_node = q.popleft()
            if g[curr_node.val][0]:
                right_node = TreeNode(g[curr_node.val][0])
                curr_node.right = right_node
                q.append(right_node)
            if g[curr_node.val][1]:
                left_node = TreeNode(g[curr_node.val][1])
                curr_node.left = left_node
                q.append(left_node)
        return root_node