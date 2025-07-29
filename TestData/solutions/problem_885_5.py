class Solution:
    def solution_885_5(self, arr: List[int]) -> int:
        n_removed = count = 0
        half_len_arr = ceil(len(arr) / 2)
        for _, n in Counter(arr).most_common():
            n_removed += 1
            count += n
            if count >= half_len_arr:
                return n_removed