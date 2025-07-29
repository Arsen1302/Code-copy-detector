class Solution:
    def solution_1049_2(self, n: int) -> str:
        ans = deque()
        while n: 
            n, d = divmod(n, 1000)
            ans.appendleft(f"{d:03}" if n else str(d))
        return ".".join(ans) or "0"