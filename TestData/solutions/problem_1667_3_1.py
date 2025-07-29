class Solution:
    def solution_1667_3_1(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # print(self.solution_1667_3_2('09-01', '10-19'))

        if arriveBob>leaveAlice or arriveAlice> leaveBob:
            return 0

        # arrive = max(arriveAlice, arriveBob)
        # leave = min(leaveAlice, leaveBob)
        # print('arrive is', arrive)
        # print('leave is', leave)

        return self.solution_1667_3_2(max(arriveAlice, arriveBob), min(leaveAlice, leaveBob))


    def solution_1667_3_2(self, start, end):
        s_m, s_d = start.split('-')
        e_m, e_d = end.split('-')

        if s_m==e_m:
            return int(e_d)-int(s_d)+1

        else:
            days = 0
            for i in range(int(s_m), int(e_m)):
                days += self.month_days[i-1]
            
            days-=int(s_d)-1
            days+=int(e_d)

            return days