class Solution:
    def solution_717_2_1(self, root: TreeNode) -> TreeNode:
        self.solution_717_2_4(root)
        self.solution_717_2_2(root)
        return root
        
    def solution_717_2_2(self, root):
        def solution_717_2_3(root):
            i = 0
            if root:
                solution_717_2_3(root.left)
                index = self.list.index(root.val)
                root.val = sum(self.list[index:])
                solution_717_2_3(root.right)
            return 0
        solution_717_2_3(root)
    
        
    def solution_717_2_4(self, root):
        self.list = []
        def solution_717_2_3(root):
            if root:
                solution_717_2_3(root.left)
                self.list.append(root.val)
                solution_717_2_3(root.right)
        solution_717_2_3(root)