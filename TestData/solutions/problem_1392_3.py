class Solution:
    def solution_1392_3(self, seats: List[int], students: List[int]) -> int:
        total_moves = 0 # taking a int variable to store the value
        sorted_seats = sorted(seats) # sorting the seat list
        sorted_students = sorted(students) #sorting the student list
        
        diff_1 = [] # taking empty list for storing difference of both the list
        for i in range(len(seats)):
            diff = abs(sorted_seats[i] - sorted_students[i]) # calculating diff of both the list elements, to calculate numbers of move. 
            diff_1.append(diff) # appending the Difference to the empty list declared by us. 
        
        for i in diff_1: # loop for traversing the diff of elems from both the lists.
            total_moves += i # adding them to calculate the moves. 
        
        return total_moves