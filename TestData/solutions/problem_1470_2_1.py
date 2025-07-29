class Solution:
    def solution_1470_2_1(self, questions: List[List[int]]) -> int:
        n = len(questions) # total number of questions
        memo = [-1] * n # memo array of size n. 
		# If memo[i] is not computed then its value must be -1 and we need to find memo[i]
		# If memo[i] != -1, this means we have already calculated this and we dont need to recompute it
        def solution_1470_2_2(index, current_val) -> int: # index is the current question number to process and current_val is the max marks upto this question
            if index >= n: # It means that we have gone through all the questions thus return the current_val
                return current_val
            if memo[index] == -1: # memo[i] == -1, not computed before and so we need to solve it
                points = questions[index][0] # points for current question
                brainpower = questions[index][1] # brainpower for current question
                a = solution_1470_2_2(index + brainpower + 1, points) # Recursive call considering we solve the current question
                b = solution_1470_2_2(index + 1, 0) # Recursive call considering we skip the current question
                memo[index] = max(a, b) # choose which ever choice yields us the best result
            return current_val+memo[index]
        return solution_1470_2_2(0, 0)