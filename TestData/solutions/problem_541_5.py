class Solution:
    def solution_541_5(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [((target - p)/s, p) for p, s in zip(position, speed)]
        time.sort(key=lambda x:-x[1])
        ans = prev = 0
        for t, _ in time:
            if t > prev:
                prev = t
                ans += 1
        return ans