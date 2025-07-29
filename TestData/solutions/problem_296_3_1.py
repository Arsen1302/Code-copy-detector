class Solution:
    def solution_296_3_1(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        def solution_296_3_2(root):
            if not root:
                return 0
            sums = root.val + solution_296_3_2(root.left) + solution_296_3_2(root.right)
            cnt[sums] += 1
            return sums
        solution_296_3_2(root)
        maxcnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxcnt]