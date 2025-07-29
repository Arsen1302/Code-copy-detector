class Solution:
    def solution_20_2(self, root: TreeNode) -> List[List[int]]:
        ans, queue = [], [root]
        while queue: 
            tmp, val = [], []
            for node in queue: 
                if node: 
                    val.append(node.val)
                    tmp.extend([node.left, node.right])
            if val: ans.append(val)
            queue = tmp
        return ans[::-1]