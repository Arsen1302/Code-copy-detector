class Solution:
    def solution_1722_4(self, nums: List[int]) -> int:
        from collections import Counter
        num_count = Counter()
        n_invalid_pairs = 0
        n_invalid_triplets = 0
        for (i, num) in enumerate(nums):
            n_invalid_triplets += (i-num_count.get(num, 0)) * num_count.get(num, 0)
            n_invalid_triplets += n_invalid_pairs
            n_invalid_pairs += num_count[num]
            num_count[num] += 1
        n_nums = len(nums)
        return n_nums * (n_nums-1) * (n_nums-2) // 6 - n_invalid_triplets