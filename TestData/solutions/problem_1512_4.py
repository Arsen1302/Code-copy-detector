class Solution:
    def solution_1512_4(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        val2node = {}
        child_set = set()
        parent_set = set()
        
        for parent_val, child_val, is_left in descriptions:
            if child_val not in val2node:
                val2node[child_val] = TreeNode(child_val)
            
            if parent_val not in val2node:
                val2node[parent_val] = TreeNode(parent_val)
                
            if is_left == 1:
                val2node[parent_val].left = val2node[child_val]
            else:
                val2node[parent_val].right = val2node[child_val]
            
            child_set.add(child_val)
            parent_set.discard(child_val)
            
            if parent_val not in child_set:
                parent_set.add(parent_val)
            else:
                parent_set.discard(parent_val)

        return val2node[parent_set.pop()]