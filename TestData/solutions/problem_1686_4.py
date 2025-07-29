class Solution:
    def solution_1686_4(self, n: int, logs: List[List[int]]) -> int:
        # each task represents an index in array (increasingly)
        # the span of task is the difference between end time of
        # preivous task and next task
        # use a hashmap with times as keys and a list to hold
        # ids
        # store all times appending ids
        # return max of time units and min of ids in list
        # time O(n) space O(n)

        d = defaultdict(list)
        start = 0
        max_val = 0

        for log in logs:
            id, end = log
            units = end - start
            max_val = max(max_val, units)
            start = end 
            d[units].append(id)

        return min(d[max_val])