class Solution:
    def solution_922_1(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = {}
        for i, j in reservedSeats: 
            if i not in seats: seats[i] = 0
            seats[i] |= 1 << j-1
        
        ans = 2 * (n - len(seats))
        for v in seats.values(): 
            if not int("0111111110", 2) &amp; v: ans += 2
            elif not int("0111100000", 2) &amp; v: ans += 1
            elif not int("0001111000", 2) &amp; v: ans += 1
            elif not int("0000011110", 2) &amp; v: ans += 1
        return ans