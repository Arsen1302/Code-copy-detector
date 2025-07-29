class Solution:
    def solution_318_5_1(self, timePoints: List[str]) -> int:
        def solution_318_5_2(time_str):
            h, m = time_str.split(':')
            return int(h)*60+int(m)
        total, minutes = 24*60, sorted([solution_318_5_2(time_str) for time_str in timePoints])
        n, diff = len(minutes), total - (minutes[-1] - minutes[0])
        for i in range(1, n):
            if (cur:=minutes[i]-minutes[i-1]) < diff: diff = cur
        return diff