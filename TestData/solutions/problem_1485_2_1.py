class Solution:
    def solution_1485_2_1(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        start_c, min_cost = str(startAt), inf

        def solution_1485_2_2(t: str) -> int:
            return (pushCost * len(t) + moveCost *
                    sum(a != b for a, b in zip(start_c + t, t)))

        for minutes in range(max(0, targetSeconds - 99) // 60,
                             ceil(targetSeconds / 60) + 1):
            seconds = targetSeconds - minutes * 60
            if -1 < minutes < 100 and -1 < seconds < 100:
                set_time = str(minutes) if minutes else ""
                set_time += f"{seconds:0>2d}" if set_time else f"{seconds}"
                min_cost = min(min_cost, solution_1485_2_2(set_time))

        return min_cost