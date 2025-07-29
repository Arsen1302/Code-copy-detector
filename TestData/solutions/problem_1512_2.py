class Solution:
    def solution_1512_2(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root = None
        table = {}
        for arr in descriptions:
            parent = arr[0]
            child = arr[1]
            isleft = arr[2]
            if table.get(parent, None) is None: # If key parent does not exist in table
                table[parent] = [TreeNode(parent), False]
            if table.get(child, None) is None: If key child does not exist in table
                table[child] = [TreeNode(child), False]
            table[child][1] = True # Since child is going to have a parent in the current iteration, set its has parent property to True
            if isleft == 1:
                table[parent][0].left = table[child][0]
            else:
                table[parent][0].right = table[child][0]
		# Now traverse the hashtable and check which node still has no parent
        for k, v in table.items():
            if not v[1]: # Has parent is False, so root is found.
                root = k
				break
        return table[root][0]