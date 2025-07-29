class Solution:
    def solution_652_1_1(self):
        self.flipped_nodes = []
        self.index = 0
        
    def solution_652_1_2(self, root: TreeNode, voyage: List[int]) -> List[int]:
        queue = deque([root])
        while queue:
            node = queue.pop()
            if not node: continue
            if node.val != voyage[self.index]: return [-1]
            self.index += 1
            if node.left and node.left.val != voyage[self.index]:
                self.flipped_nodes.append(node.val)
                node.left, node.right = node.right, node.left
            queue.append(node.right), queue.append(node.left)
        return self.flipped_nodes