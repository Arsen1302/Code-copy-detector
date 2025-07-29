class Solution:
    def solution_1149_4(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students) # making provided list as queue for performing operation. 
        sandwhiches = deque(sandwiches) # making provided list as queue for performing operation. 
        count = 0 # taking a counter to count uneaten students. 
        while count < len(students): # counter(uneaten) should always be less then total student.  
            if students[0] == sandwhiches[0]: # if yes, then remove the element from both the queue. 
                sandwhiches.popleft() # removing element from sandwiches queue.
                count = 0 # making counter zero as student took the sandwiches provided. 
            else:
                students.append(students[0]) # if students dont take the sandwich, then its getting at the end of the queue(student queue).
                count += 1 # 
            students.popleft() # there are two uses of it. 1) Once student take the sandwich and leave 2) When student dont take the sandwich and we move them to last of the queue.
        return len(students) # this will give us the total student how didnt eat.