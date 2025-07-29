class Solution:
    def solution_1633_3(self, tasks: List[int], space: int) -> int:
        day_checker = {}
        day = 1
        for i in range(len(tasks)):
            if tasks[i] not in day_checker:
                day_checker[tasks[i]] = day
            else:
                if abs(day_checker[tasks[i]] - day) <= space:
                    day = day_checker[tasks[i]] + space + 1
                    day_checker[tasks[i]] = day 
                else:
                    day_checker[tasks[i]] = day
              day += 1       
        return day - 1
		```