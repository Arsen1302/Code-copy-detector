class Solution:
    def solution_559_2_1(self, root1: TreeNode, root2: TreeNode) -> bool:
        def solution_559_2_2(rt: TreeNode):
            if (None, None) == (rt.left, rt.right):
                yield rt.val
            else:
                if rt.left:
                    yield from solution_559_2_2(rt.left)
                if rt.right:
                    yield from solution_559_2_2(rt.right)

        return all(l1 == l2 for l1, l2 in itertools.zip_longest(solution_559_2_2(root1), solution_559_2_2(root2)))