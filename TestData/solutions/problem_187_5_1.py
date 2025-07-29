class Solution:
    def solution_187_5_1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def solution_187_5_2(n1):
            for n2 in nums2:
                yield [n1+n2, n1, n2]
        merged = heapq.merge(*map(solution_187_5_2, nums1))
        return [p[1:] for p in itertools.islice(merged, k) if p]