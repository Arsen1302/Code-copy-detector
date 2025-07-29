class Solution:
    def solution_890_5(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes / 60 * 360 
        hours_angle = hour / 12 * 360 + minutes / 60 * 30 
        if minutes_angle  > hours_angle:
            angle =  minutes_angle - hours_angle
            return min(angle, 360 - angle)
        else:
            angle = hours_angle - minutes_angle
            return min(angle, 360 - angle)