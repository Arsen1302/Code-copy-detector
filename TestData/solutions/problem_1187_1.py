class Solution:
    def solution_1187_1(self, s: str) -> int:
        dd = deque(s)
        while len(dd) >= 2 and dd[0] == dd[-1]:
            ch = dd[0]
            while dd and dd[0] == ch: dd.popleft()
            while dd and dd[-1] == ch: dd.pop()
        return len(dd)