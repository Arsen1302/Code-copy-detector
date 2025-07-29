class Solution:
                        # The plan here is to solution_88_2_2 the tree, right-first
                        # (opposite of  the usual left-first method), and
                        # keeping track of the tree levels as we proceed. The 
                        # first node we visit on each level is the right-side view 
                        # node. We know it's the first because the level will be
                        # one greater than the length of the current answer list.

    def solution_88_2_1(self, root: TreeNode) -> list[int]:
        ans =[]
        
        def solution_88_2_2(node =root,level=1):
            if not node: return
            
            if len(ans) < level: 
                ans.append(node.val)
            solution_88_2_2(node.right,level+1)         #  <--- right first
            solution_88_2_2(node.left ,level+1)         #  <--- then left

            return 

        solution_88_2_2()
        return ans