class Solution:
    def solution_1329_4_1(self, current_score, current_student, available_mentors, n, all_scores):
        if current_student == n:
            return current_score
        return max([
            self.solution_1329_4_1(
                current_score + all_scores[(current_student, mentor)],
                current_student + 1,
                available_mentors - {mentor},
                n,
                all_scores
            )
            for mentor in available_mentors
        ])

    def solution_1329_4_2(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        all_scores = {
            (idx, jdx): sum([
                int(student_answer == mentor_answer)
                for student_answer, mentor_answer
                in zip(students[idx], mentors[jdx])
            ])
            for idx in range(len(students))
            for jdx in range(len(mentors))
        }
        return self.solution_1329_4_1(0, 0, set(range(len(students))), len(students), all_scores)