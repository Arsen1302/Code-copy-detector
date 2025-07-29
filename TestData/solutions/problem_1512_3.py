class Solution:
    def solution_1512_3(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        tree = dict()
        children = set()
        for parent, child, isLeft in descriptions:
            if parent not in tree : tree[parent] = TreeNode(parent)
            if child not in tree : tree[child] = TreeNode(child)
            
            if isLeft : tree[parent].left = tree[child]
            else : tree[parent].right = tree[child]
        
            children.add(child)
        
        for parent in tree:
            if parent not in children:
                return tree[parent]