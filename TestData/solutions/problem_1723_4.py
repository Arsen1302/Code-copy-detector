class Solution:
    def solution_1723_4(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []
        node = root 
        stack = []
        while node or stack: 
            if node: 
                stack.append(node)
                node = node.left
            else: 
                node = stack.pop()
                vals.append(node.val)
                node = node.right 
        ans = []
        for q in queries:  
            ans.append([-1, -1])
            lo = bisect_right(vals, q)-1
            if 0 <= lo: ans[-1][0] = vals[lo]
            hi = bisect_left(vals, q)
            if hi < len(vals): ans[-1][1] = vals[hi]
        return ans