class Solution:
    def solution_922_3(self, n: int, reserved: List[List[int]]) -> int:
        r = defaultdict(int)
        for row, seat in reserved:
            if 2 <= seat <= 9:
                r[row] |= 1 << (seat-2)
        ans = 0
        for _, v in r.items():
            ans += int(any(not v &amp; mask for mask in [0xf, 0xf0, 0x3c]))
        return ans + (n - len(r)) * 2