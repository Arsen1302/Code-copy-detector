class Solution:
    def solution_1423_4(self, plants: list[int], capacity: int) -> int:
        steps = 1  # the first step from -1 to 0
        cur_capacity = capacity
        for i in range(len(plants) - 1):
            cur_capacity -= plants[i]  # watering the current plant
            if cur_capacity < plants[i + 1]:  # if water isn't enough
                steps += (i + 1) * 2 + 1 # steps from i to -1 then from -1 to i + 1
                cur_capacity = capacity  # restore the capacity
            else:
                steps += 1  # just move forward
        return steps