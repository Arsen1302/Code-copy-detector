class Solution:
    def solution_1633_5(self, tasks: List[int], space: int) -> int:
        day = 1
        allowed = dict()
        space1 = space + 1
        for task in tasks:
            if task in allowed:
                if day >= allowed[task]:
                    allowed[task] = day + space1
                else:
                    day = allowed[task]
                    allowed[task] = day + space1
            else:
                allowed[task] = day + space1
            day += 1
        return day - 1