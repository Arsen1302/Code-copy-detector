class Solution:
    def solution_1149_3(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while len(students) > count:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            else:
                students.append(students[0])
                count+=1

            students.pop(0)
        return len(students)
		
#Upvote will be encouraging.