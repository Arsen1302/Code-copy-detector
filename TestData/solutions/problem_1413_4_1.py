class Solution:
    def solution_1413_4_1(self, n: int, quantities: List[int]) -> int:
        search_range = range(1, max(quantities))
        return bisect.bisect_left(search_range, 1,
            key=lambda x: self.solution_1413_4_2(n, quantities, x)) + 1


    def solution_1413_4_2(self, n: int, quantities: List[int], k: int) -> bool:
        quantities_gt_k = [q for q in quantities if q > k]
        num_qs_lt_k = len(quantities) - len(quantities_gt_k)
        extra_shops = sum(math.ceil(q / k) for q in quantities_gt_k)
        min_num_shops = num_qs_lt_k + extra_shops
        return n >= min_num_shops