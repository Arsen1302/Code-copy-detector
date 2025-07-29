class Solution:
    def solution_1686_5(self, n: int, logs: list[list[int]]) -> int:
        """
            TC: O(n)
            SC: O(1)
        """
        longest_time = 0
        longest_time_id = 0
        pre_leave_time = 0
        for _id, leave_time in logs:
            worked_time = leave_time - pre_leave_time
            pre_leave_time = leave_time
            if worked_time > longest_time:
                longest_time = worked_time
                longest_time_id = _id
            elif worked_time == longest_time and longest_time_id > _id:
                longest_time_id = _id
        return longest_time_id