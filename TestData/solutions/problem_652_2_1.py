class Solution:
    def solution_652_2_1(self):
        self.flipped_nodes = []
        self.index = 0
        self.flag = False
        
    def solution_652_2_2(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def solution_652_2_3(node = root):
            if not node: return
            if node.val != voyage[self.index]:
                self.flag = True
                return
            self.index += 1
            if node.left and node.left.val != voyage[self.index]:
                self.flipped_nodes.append(node.val)
                node.left, node.right = node.right, node.left
            solution_652_2_3(node.left), solution_652_2_3(node.right)

        solution_652_2_3()
        return self.flipped_nodes if not self.flag else [-1]