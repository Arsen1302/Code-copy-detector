class Solution:
    def solution_1690_5(self, time: str) -> int:

        # hours
        if time[:2] == "??":
            combinations = 24
        elif time[1] == "?":
            if time [0] in "01":
                combinations = 10
            else:
                combinations = 4
        elif time[0] == "?" and time[1] in "0123":
            combinations = 3
        elif time[0] == "?" and time[1] in "456789":
            combinations = 2
        else:
            combinations = 1

        # minutes
        if time[3] == "?": combinations *= 6
        if time[4] == "?": combinations *= 10

        return combinations