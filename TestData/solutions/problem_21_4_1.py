class Solution:
    def solution_21_4_1(self, nums: List[int]) -> TreeNode:
        def solution_21_4_2(l, r):
            # base case, l must always be <= r
            # l == r is the case of a leaf node.
            if l > r: return None
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = solution_21_4_2(l, mid-1)
            node.right = solution_21_4_2(mid+1, r)
            return node
        # both the indices are inclusive,
        # mathematically given by: [0, len(nums)-1]
        return solution_21_4_2(0, len(nums)-1)