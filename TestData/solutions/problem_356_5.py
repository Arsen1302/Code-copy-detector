class Solution:
    def solution_356_5(self, t: TreeNode) -> str:
        if not t:
            return ''
        if not t.right and not t.left:
            return f'{t.val}'
        elif not t.right:
            return f'{t.val}({self.solution_356_5(t.left)})'        
        return f'{t.val}({self.solution_356_5(t.left)})({self.solution_356_5(t.right)})'
	```