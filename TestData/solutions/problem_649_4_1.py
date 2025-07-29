class Solution(object):
    def solution_649_4_1(self, root):
        result = [0]
        
        # 0 indicates that it doesn't need cam which might be a leaf node or a parent node which is already covered
        # < 3 indicates that it has already covered
        # >= 3 indicates that it needs a cam
        
        def solution_649_4_2(root):
            if not root:
                return 0
            needsCam = solution_649_4_2(root.left) + solution_649_4_2(root.right)
            
            if needsCam == 0:
                return 3
            if needsCam < 3:
                return 0
            result[0]+=1
            return 1
         
        return result[0] + 1 if solution_649_4_2(root) >= 3 else result[0]