class Solution:
    def solution_890_3(self, hour: int, minutes: int) -> float:
        
        # Normalizing minute position in range (1-12)
        min_clock = minutes/5

        # If time is 12.00 returning 0
        if minutes == 0 and hour*30 == 360:
            return 0
        
        # If minutes is 0 then multiply hour by 30 degree as each hour consists of 30 degree
        elif minutes == 0:
            only_hour = hour*30
            
            # Check whether it is shorter in opposite direction
            if only_hour > 180:
                return 360-(only_hour)
            return only_hour
        
        else:
            # Finding the degree between minute hand and closest hour of the hour hand
            time = abs(hour-min_clock)*30
            
            # Finding the difference that needs to added/subtracted
            diff = 30/(60/minutes)
            
            # Subtracting when minute hand is at greater value that hour hand
            if min_clock > hour:
                fin_time = time-diff
                
            # Adding when minute hand is at lesser value that hour hand
            else:
                fin_time = time+diff
            
            # Check the shorter direction
            if fin_time > 180:
                diff = fin_time-180
                return abs(180-diff)
            else:
                return abs(fin_time)