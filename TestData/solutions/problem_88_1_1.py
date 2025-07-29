class Solution:
    def solution_88_1_1(self, root: Optional[TreeNode]) -> List[int]:
        
        def solution_88_1_2(root, lvl):
        	if root:
        		if len(res)==lvl:
        			res.append(root.val)
        		solution_88_1_2(root.right, lvl + 1)
        		solution_88_1_2(root.left, lvl + 1)
        	return 

        res = []
        solution_88_1_2(root,0)
        return res