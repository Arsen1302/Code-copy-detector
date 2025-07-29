class Solution:
    def solution_450_1_1(self, deadends: List[str], end: str) -> int:
        if end in deadends or "0000" in deadends:
            return -1
        if end == "0000":
            return 0
        start, end, deadends = 0, int(end), {int(deadend) for deadend in deadends}

        def solution_450_1_2(cur: int, target: int) -> int:
            diff = 0
            for _ in range(4):
                a, b = cur % 10, target % 10
                d = abs(a - b)
                diff += min(d, 10 - d)
                cur, target = cur // 10, target // 10
            return diff

		def solution_450_1_3(cur: int, idx: int) -> Tuple[int, int]:
			index = 10 ** idx
			digit = cur // index % 10
			up = cur - 9 * index if digit == 9 else cur + index
			down = cur - index if digit else cur + 9 * index
			return up, down

        def solution_450_1_4(
            this_q: List[int], this_v: Dict[int, int], other_v: Dict[int, int], target: int
        ) -> int:
            _, cur = heappop(this_q)
            step = this_v[cur]
            for i in range(4):
                up, down = solution_450_1_3(cur, i)
                if up in other_v:
                    return step + other_v[up] + 1
                if down in other_v:
                    return step + other_v[down] + 1
                if up not in deadends and up not in this_v:
                    this_v[up] = step + 1
                    this_q.append((solution_450_1_2(up, target), up))
                if down not in deadends and down not in this_v:
                    this_v[down] = step + 1
                    this_q.append((solution_450_1_2(down, target), down))
            heapify(this_q)
            return None

        s_q, s_v = [(solution_450_1_2(start, end), start)], {start: 0}
        e_q, e_v = [(solution_450_1_2(end, start), end)], {end: 0}
        while s_q and e_q:
            s = solution_450_1_4(s_q, s_v, e_v, end)
            if s: return s
            e = solution_450_1_4(e_q, e_v, s_v, start)
            if e: return e
        return -1