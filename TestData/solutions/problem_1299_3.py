class Solution:
    def solution_1299_3(self, startTime: str, finishTime: str) -> int:

        start=startTime.split(":")
        startHour,startMin=int(start[0]),int(start[1])
        
        end=finishTime.split(":")
        endHour,endMin=int(end[0]),int(end[1])
        # if start time is greater than endtime, calculate round till 00:00 and then till finish time
        if (startHour>endHour ) or (startHour==endHour and startMin >endMin):
            return (24-startHour-1)*4+(60-startMin)//15 +self.solution_1299_3("00:00",finishTime)
        else:
            if startMin not in [0,15,30,45]:
                if startMin<15:startMin=15
                elif startMin<30:startMin=30
                elif startMin<45:startMin=45
                elif startHour!=23:
                    startMin=0
                    startHour+=1
                else:
                    startMin=0
                    startHour=0

            if endHour==startHour:return (endMin-startMin)//15
            else:
                return (endHour-startHour)*4+(endMin-startMin)//15