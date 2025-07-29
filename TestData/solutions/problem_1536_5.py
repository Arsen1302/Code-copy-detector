class Solution:
    def solution_1536_5(self, num: int) -> int:
        heap_odd, heap_even, res = [], [], []
        for n in str(num):
            heappush(heap_even, -int(n)) if int(n) % 2 == 0 else heappush(heap_odd, -int(n))
        for n in str(num):
            res.append(str(-heappop(heap_even))) if int(n) % 2 == 0 else res.append(str(-heappop(heap_odd)))
        return int(''.join(res))