class Solution:
    
    def solution_717_3_1(self, node):
        if node is not None:
            yield from self.solution_717_3_1(node.right)
            yield node
            yield from self.solution_717_3_1(node.left)
    
    def solution_717_3_2(self, root: TreeNode) -> TreeNode:
        current_sum = 0
        for node in self.solution_717_3_1(root):
            current_sum += node.val
            node.val = current_sum
        return root