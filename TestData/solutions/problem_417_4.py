class Solution:
    def solution_417_4(self, root: TreeNode, val: int) -> TreeNode:
        cur_node = root
        while True:
            if val > cur_node.val:
                if cur_node.right == None:
                    cur_node.right = TreeNode(val)
                    break
                else:
                    cur_node = cur_node.right
            if val < cur_node.val:
                if cur_node.left == None:
                    cur_node.left = TreeNode(val)
                    break
                else:
                    cur_node = cur_node.left
        return root