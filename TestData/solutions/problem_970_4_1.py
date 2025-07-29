class Solution:
    def solution_970_4_1(self, root: TreeNode) -> int:
        maxx = root.val
        count = 0
        def solution_970_4_2(node,maxx):
            nonlocal count
            if node is None:
                return
            if node.val >= maxx:
                count +=1
                maxx = node.val
            solution_970_4_2(node.left,maxx)
            solution_970_4_2(node.right,maxx)
            return
        solution_970_4_2(root,maxx)
        return count