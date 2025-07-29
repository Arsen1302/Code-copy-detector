class Solution:
    def solution_1177_2(self, time: str) -> str:
        maxTime = "23:59" if time[0] in "?2" and time[1] in "?0123" else "19:59"
        return "".join(t if t != "?" else m for t, m in zip(time, maxTime))