class Solution:
    def solution_1080_5(self, logs: List[str]) -> int:
        steps = 0
        for i in logs:
            if i == "../" and steps != 0:
                steps -= 1
            elif i == "./" or i == "../" and steps == 0:
                continue
            else:
                steps += 1
        return steps