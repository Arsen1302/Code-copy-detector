class Solution:
    def solution_26_5_1(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        result = []
        
        def solution_26_5_2(root, target, path):   
            if not root:
                return
            if not root.left and not root.right and target - root.val == 0:
                result.append(path + [root.val])
                return
            
            solution_26_5_2(root.left, target - root.val, path + [root.val])
            solution_26_5_2(root.right, target - root.val, path + [root.val])
        
        solution_26_5_2(root, target, [])
        return result