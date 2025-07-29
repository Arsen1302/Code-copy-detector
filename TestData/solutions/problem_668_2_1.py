class Solution:
    def solution_668_2_1(self, root: TreeNode) -> str:
        paths = []
        
        def solution_668_2_2(node, string):
            # Translate node value to letter via ASCII
            string += chr(node.val + 97)
            
            if node.left: solution_668_2_2(node.left, string)
            if node.right: solution_668_2_2(node.right, string)
            # At leaf node, add reversed tree path to "paths"
            if not node.right and not node.left: paths.append(string[::-1])
                
        solution_668_2_2(root, '')
        # Sort in lexicographical order and return first path
        paths.sort()
        return paths[0]