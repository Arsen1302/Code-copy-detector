class Solution:
    def solution_986_1(self, n: int, connections: List[List[int]]) -> int:
        cmap = {0}
        count = 0
        dq = deque(connections)
        while dq:
            u, v = dq.popleft()
            if v in cmap:
                cmap.add(u)
            elif u in cmap:
                cmap.add(v)
                count += 1
            else:
                dq.append([u, v])
        return count