class Solution:
    def solution_1667_4_1(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        monthDatesMap = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        # need a helper function to compare two dates
        def solution_1667_4_2(date1, date2):
            # check if date1 >= date2
            month1 = int(date1[0:2])
            month2 = int(date2[0:2])
            if month1 > month2:
                return(True)
            elif month1 == month2:
                if int(date1[3:]) >= int(date2[3:]):
                    return(True)
            return(False)
        
        def solution_1667_4_3(date1, date2):
            # make sure date2 is >= date1
            month1 = int(date1[0:2])
            month2 = int(date2[0:2])
            dateDiff = 0
            if month2 == month1:
                dateDiff = int(date2[3:]) - int(date1[3:]) + 1
            else:
                for tempMonth in range(month1, month2):
                    if tempMonth == month1:
                        dateDiff += (monthDatesMap[tempMonth] - int(date1[3:]) + 1)
                    else:
                        dateDiff += monthDatesMap[tempMonth]
                dateDiff += int(date2[3:])
            return(dateDiff)

        # figure out who arrives earlier
        if solution_1667_4_2(arriveAlice, arriveBob):
            # Bob arrives earlier
            earlierPersonArrival = arriveBob
            earlierPersonLeave = leaveBob
            laterPersonArrival = arriveAlice
            laterPersonLeave = leaveAlice
        else:
            # Alice arrives earlier
            earlierPersonArrival = arriveAlice
            earlierPersonLeave = leaveAlice
            laterPersonArrival = arriveBob
            laterPersonLeave = leaveBob
        

        if not solution_1667_4_2(earlierPersonLeave, laterPersonArrival):
            # if earlier person leaves stricly before later personal arrival
            return(0)
        else:
            # if earlier person leaves later than later person arrival
            if solution_1667_4_2(earlierPersonLeave, laterPersonLeave):
                # earlier person leaves later
                print((laterPersonLeave, earlierPersonLeave))
                return(solution_1667_4_3(laterPersonArrival, laterPersonLeave))
            else:
                # earlier person also leaves earilier
                return(solution_1667_4_3(laterPersonArrival, earlierPersonLeave))