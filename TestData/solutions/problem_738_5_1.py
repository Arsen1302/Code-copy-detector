class Solution:
    def solution_738_5_1(self, root: TreeNode, limit: int) -> TreeNode:
        # recursive dfs
        # helper function takes node, path sum, returns node
        # if leaf (no kids), check if over limit; if not return null
        # else, solution_738_5_2 into kids; and reassign with their return call
        # if at one point you had kids, but now do not, return None (purge me)
        # (kids to no kids implies no root to leaf path exists over limit)
        # O(N) time, O(H) tree height call space

        def solution_738_5_2(node: TreeNode, path: int) -> TreeNode:
            if not node: return None

            if not node.left and not node.right:
                return None if (path + node.val) < limit else node

            node.left = solution_738_5_2(node.left, path + node.val)
            node.right = solution_738_5_2(node.right, path + node.val)

            return None if not node.left and not node.right else node

        # setup and call
        return solution_738_5_2(root, 0)