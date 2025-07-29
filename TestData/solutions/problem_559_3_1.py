class Solution:
    def solution_559_3_1(self, root1: TreeNode, root2: TreeNode) -> bool:
        def solution_559_3_2(rt: TreeNode):
            stack = [rt]
            while stack:
                node = stack.pop()
                if (None, None) == (node.left, node.right):
                    yield node.val
                else:
                    if node.right:
                        stack += node.right,
                    if node.left:
                        stack += node.left,

        return all(l1 == l2 for l1, l2 in itertools.zip_longest(solution_559_3_2(root1), solution_559_3_2(root2)))