class Solution:
    def solution_1524_3_1(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_score = [0, None]
        def solution_1524_3_2(i, remaining, score, arrows):
		    # Base case. Update max score.
            if remaining == 0 or i == -1:
                if score > max_score[0]:
                    max_score[0] = score
                    max_score[1] = arrows[:]
                return

			# Special handling for the last section. Use up all the arrows.
            if i == 0:
                arrows[i] = remaining
                solution_1524_3_2(i - 1, 0, score + i, arrows)
                arrows[i] = 0
                return

		    # Try to compete with Alice if there are enough arrows.
            arrowsNeeded = aliceArrows[i] + 1
            if remaining >= arrowsNeeded:
                arrows[i] = arrowsNeeded
                solution_1524_3_2(i - 1, remaining - arrowsNeeded, score + i, arrows)
                arrows[i] = 0

            # Skip this section and go to the next section.
            solution_1524_3_2(i - 1, remaining, score, arrows)
        
		# Kick off the recursion
        solution_1524_3_2(len(aliceArrows) - 1, numArrows, 0, [0 for _ in aliceArrows])
        return max_score[1]