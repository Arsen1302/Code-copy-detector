class Solution:
    def solution_249_2(self, root: TreeNode, key: int) -> TreeNode:
        # search for node
        node = root
        parent = left = None
        while node:
            if node.val < key: parent, node, left = node, node.right, False
            elif node.val > key: parent, node, left = node, node.left, True
            else: break # found 
        
        # delete the node 
        if node: # if found 
            if not node.left or not node.right: 
                if parent: 
                    if left: parent.left = node.left or node.right
                    else: parent.right = node.left or node.right
                else: return node.left or node.right
            else: 
                temp = parent = node
                node = node.left 
                if not node.right: parent.left = node.left
                else: 
                    while node.right: parent, node = node, node.right
                    parent.right = node.left
                temp.val = node.val
        return root