class Solution:
    def solution_652_5(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans = []
        stack = [root]
        k = 0
        while stack: 
            node = stack.pop()
            if node: 
                if node.val != voyage[k]: return [-1] # impossible 
                k += 1
                if node.right and node.right.val == voyage[k]: 
                    if node.left: ans.append(node.val)
                    stack.extend([node.left, node.right])
                else: 
                    stack.extend([node.right, node.left])
        return ans