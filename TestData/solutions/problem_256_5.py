class Solution:
    def solution_256_5(self, nums: List[int]) -> bool:
        """So we have been having trouble finding a decent way to tell the size
        of the loop and reject a loop if its size is 1. This solution

        Ref: https://leetcode.com/problems/circular-array-loop/discuss/232417/Python-simple-solution-beats-100-with-O(1)-space

        offers a simple idea to identify a size-one loop: check whether the
        next index is the same as the current one. This way, we don't have to
        keep record of the link size. We can return true for all loops except
        those whose next index is the same as the current.

        We also create a marker for each traversal. Once we hit an index with
        the same marker of the current traversal, we know for sure that a loop
        of size larger than one has been found.

        O(N) time, O(1) space. 51 ms, 63% ranking.
        """
        N = len(nums)
        for i in range(N):
            marker, j, direction = 1001 + i, i, nums[i]
            while -1000 <= nums[j] <= 1000:
                if direction * nums[j] > 0:  # point to same direction
                    next_j = (j + nums[j] + N) % N
                    if next_j == j:  # loop of size 1, do not assign marker
                        break
                    nums[j], j = marker, next_j
                else:
                    break
            if nums[j] == marker:
                return True
        return False