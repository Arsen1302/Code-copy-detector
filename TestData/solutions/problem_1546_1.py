class Solution:
    def solution_1546_1(self, tasks: List[int]) -> int:
        table, res = Counter(tasks), 0 # Counter to hold frequency of ith task and res stores the result.
        for count in table.values():
            if count <= 1: return -1 # If count <= 1 then it cannot follow the condition hence return -1.
            res += ceil(count / 3) # Total number of groups increments after 3 values. 
        return res