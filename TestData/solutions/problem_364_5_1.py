class Solution:
    def solution_364_5_1(self, courses: List[List[int]]) -> int:
        # First, sorting according to the lastday.
        courses.sort(key=lambda x: x[1])
        memo = [[-1 for _ in range(courses[-1][1] + 1)] for _ in range(len(courses) + 1)]
        return self.solution_364_5_2(courses, 0, 0, memo)
    # Hypothesis, will return maximum number of courses taken
    def solution_364_5_2(self, courses, totalDays, index, memo) -> int:
        # Returning 0, if no courses to take
        if index >= len(courses):
            return 0
        if memo[index][totalDays] != -1:
            return memo[index][totalDays]
        # Curr Course
        currCourse = courses[index]
        # We will have two choices now, after sorting, Either take the current course or not
        courseTaken = 0
        courseNotTaken = 0
        # If we take the course, we will increase the count by 1
        if totalDays + currCourse[0] <= currCourse[1]:
            courseTaken = 1 + self.solution_364_5_2(courses, totalDays + currCourse[0], index + 1, memo)
        # If not taking course, go to next course, and dont increase the count
        courseNotTaken = self.solution_364_5_2(courses, totalDays, index + 1, memo)
        # return maximum of course Taken and  not taken
        memo[index][totalDays] = max(courseTaken, courseNotTaken)
        return memo[index][totalDays]