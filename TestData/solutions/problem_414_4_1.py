class Solution:
    def solution_414_4_1(self, nums: List[int], k: int) -> bool:
        n, expected_sum = len(nums), sum(nums) / k
        nums.sort(reverse=True)
        if expected_sum != int(expected_sum) or nums[0] > expected_sum:
            return False

        def solution_414_4_2(pos, target, done):
            if done == k-1: return True
            if pos == n: return False
            num = nums[pos]
            if num > target:
                return solution_414_4_2(pos + 1, target, done)
            nums[pos] = expected_sum + 1
            if num == target:
                return solution_414_4_2(0, expected_sum, done + 1)
            if solution_414_4_2(pos + 1, target - num, done): return True
            nums[pos] = num
            return solution_414_4_2(pos + 1, target, done)

        return solution_414_4_2(0, expected_sum, 0)