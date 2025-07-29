class Solution:
    def solution_576_1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mp = {x: i for i, x in enumerate(inorder)} # relative position 
		root = None
	    stack = []
        for x in preorder: 
            if not root: root = node = TreeNode(x)
            elif mp[x] < mp[stack[-1].val]: stack[-1].left = node = TreeNode(x)
            else: 
                while stack and mp[stack[-1].val] < mp[x]: node = stack.pop() # retrace 
                node.right = node = TreeNode(x)
            stack.append(node)
        return root