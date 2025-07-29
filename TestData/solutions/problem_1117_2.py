class Solution:
    def solution_1117_2(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        visited = set()
        limit = max(x, max(forbidden)) + a + b
        queue = [(0, 0, False)]
        while queue:
            pos, step, back = queue.pop(0)
            if pos > limit or pos < 0 or pos in forbidden or (pos, back) in visited:
                continue
            if pos == x:
                return step
            queue.append((pos+a, step+1, False))
            if not back: queue.append((pos-b, step+1, True))
            visited.add((pos, back))
        return -1