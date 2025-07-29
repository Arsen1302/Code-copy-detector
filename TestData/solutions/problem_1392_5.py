class Solution:
    def solution_1392_5(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        c,n=0,len(seats)
        for i in range(n): c+=abs(seats[i]-students[i])
        return c