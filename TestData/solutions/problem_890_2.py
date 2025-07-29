class Solution:
    def solution_890_2(self, h, m):
        # Convert the hour hand to another minute hand
        m2 = (h%12 + m/60)*5
        
        # Calculate the difference between the two minute hands
        diff = abs(m-m2)
        
        # Convert the difference to an angle
        ang = diff*(360/60)
        
        # Return the smallest angle
        return min(360-ang, ang)