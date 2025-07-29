class Solution:
    def solution_1149_5(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches: # Till the time we have sandwiches we`ll run this loop.
            if sandwiches[0] in students: # Now we`ll check if sandwich element are in student or not. In both the list we`ll be having 0`s and 1s, either student take a sandwich or not , either a student take a cicular sandwich or a square one.
                students.remove(sandwiches[0]) # Once we found remove the element from student that matches in sandwiches.
                sandwiches.pop(0) # Once we found remove the element from sandwiches that matches in student.
            else:
				break # in case we dont have matching elements, we`ll break the loop. 
        return len(students) # then we`ll return how many students finally eat or not.