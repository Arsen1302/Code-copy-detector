class Solution:
    def solution_1529_5(self, start: int, goal: int) -> int:
        b_start = str(bin(start))[2:]
        b_goal = str(bin(goal))[2:]
        ans = 0
        if len(b_start) < len(b_goal):
            b_start = '0' * (len(b_goal) - len(b_start)) + b_start
        elif len(b_start) > len(b_goal):
            b_goal = '0' * (len(b_start) - len(b_goal)) + b_goal
        for i in range(len(b_goal)):
            if b_goal[i] != b_start[i]:
                ans += 1
        return  ans