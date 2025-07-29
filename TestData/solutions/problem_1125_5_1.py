class Solution:
    def solution_1125_5_1(self, tasks: List[List[int]]) -> int:
        def solution_1125_5_2(a): #creating a custom sorting function (we want to sort by difference ~ from the biggest to the smallest)
            return a[0]-a[1]


        tasks.sort(key=solution_1125_5_2)
        my_energy = tasks[0][1] # how much we need to have at the start
        current_task = tasks[0][1] - tasks[0][0] # how much remains after we finish the first task
        for i in range(1, len(tasks)):
            if current_task < tasks[i][1]:
                my_energy += tasks[i][1] - current_task # how much we need to add in order to get the minimum to start the current task
                current_task += tasks[i][1] - current_task
            current_task -= tasks[i][0] # how much we have after finishing the current task
        return my_energy