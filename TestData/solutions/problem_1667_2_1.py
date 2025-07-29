class Solution:
    def solution_1667_2_1(self, time):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days[:int(time.split('-')[0]) - 1]) + int(time.split('-')[1])

    def solution_1667_2_2(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice = [self.solution_1667_2_1(arriveAlice), self.solution_1667_2_1(leaveAlice)]
        bob = [self.solution_1667_2_1(arriveBob), self.solution_1667_2_1(leaveBob)]
        if bob[0] <= alice[0] <= bob[1]:
            if bob[1] <= alice[1]:
                return bob[1] - alice[0] + 1
            else:
                return alice[1] - alice[0] + 1
        elif alice[0] <= bob[0] <= alice[1]:
            if alice[1] <= bob[1]:
                return alice[1] - bob[0] + 1
            else:
                return bob[1] - bob[0] + 1
        else:
            return 0