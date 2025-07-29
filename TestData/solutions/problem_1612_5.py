class Solution:
    def solution_1612_5(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        freq = Counter(abs(x1-x2) for x1, x2 in zip(nums1, nums2) if x1 != x2)
        pq = [(-k, v) for k, v in freq.items()]
        heapify(pq)
        k1 += k2
        while pq and k1: 
            x, v = heappop(pq)
            if pq: xx, vv = heappop(pq)
            else: xx = vv = 0
            diff = xx - x
            if diff * v <= k1: 
                k1 -= diff * v 
                if vv: heappush(pq, (xx, v+vv))
            else: 
                q, r = divmod(k1, v)
                k1 = 0
                heappush(pq, (x+q+1, r))
                heappush(pq, (x+q, v-r))
                if vv: heappush(pq, (xx, vv))
        return sum(x*x*v for x, v in pq)