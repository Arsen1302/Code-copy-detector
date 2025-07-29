class Solution:
    def solution_368_5(self, root: Optional[TreeNode]) -> List[float]:
        # Store in a stack the root node and its level (i.e. 0)
        stack = [(root, 0)]
        
        # Dict used to contain values at same tree level
        level_values = defaultdict(list)
        
        # Explore the tree
        while stack:
            current_node, current_level = stack.pop()
            
            # Append current node value to the list contained inside dict at current tree level
            level_values[current_level].append(current_node.val)
            
            # If present, add right node to the stack and increase level by one
            if current_node.right:
                stack.append((current_node.right, current_level+1))
            
            # If present, add left node to the stack and increase level by one
            if current_node.left:
                stack.append((current_node.left, current_level+1))
        
        # List comprehension to compute mean value for each level by using dict information
        return [sum(v)/len(v) for v in level_values.values()]