class Solution:
    def solution_423_4(self, nums: List[int], k: int) -> int:

        prefix, result = [1] + list(itertools.accumulate(nums, operator.mul)), 0

        for i in range(1, len(prefix)):                        
            for j in range(0, i):
                if prefix[i] // prefix[j] < k:
                    result += (i-j)
                    break

        return result