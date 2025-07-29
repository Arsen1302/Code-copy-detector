class Solution:
    def solution_890_4(self, hour: int, minutes: int) -> float:
        angle = abs((hour + (minutes / 60)) - (minutes/5)) * 30

        if angle > 180:
            angle = 360 - angle

        return angle