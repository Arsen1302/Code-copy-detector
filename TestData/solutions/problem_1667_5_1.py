class Solution:
    def solution_1667_5_1(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def solution_1667_5_2(date):
            a,b = map(int,date.split("-"))
            return sum(month[0:a-1])+b
        arriveAlice = solution_1667_5_2(arriveAlice)
        leaveAlice = solution_1667_5_2(leaveAlice)
        arriveBob = solution_1667_5_2(arriveBob)
        leaveBob = solution_1667_5_2(leaveBob)
        left = max(arriveAlice, arriveBob)
        right = min(leaveAlice,leaveBob)
        return max(0,right-left+1)