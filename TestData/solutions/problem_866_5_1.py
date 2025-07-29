class Solution:
    def solution_866_5_1(self, root: TreeNode) -> int:
        evenGrandParent = []
        
        def solution_866_5_2(node, parent=None, grandParent=None):
            if node is None:
                return
            
            if grandParent and grandParent % 2 == 0:
                nonlocal evenGrandParent
                evenGrandParent.append(node.val)
            
            solution_866_5_2(node.right, node.val, parent)
            solution_866_5_2(node.left, node.val, parent)
        
        
        solution_866_5_2(root)
        
        return sum(evenGrandParent)