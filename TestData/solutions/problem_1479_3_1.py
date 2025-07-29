class Solution:
    def solution_1479_3_1(self, statements: List[List[int]]) -> int:
        n = len(statements)
        self.ans = 0
		# good candidate set for O(1) lookup
        good = set()
        
        def solution_1479_3_2(idx, count):
            if idx == n:
				# found a potential solution
                self.ans = max(self.ans, count)
                return
            
            # assume idx is good
            good.add(idx)
            for i in range(idx):
				# check for any contradictions with previous assumptions
                if (statements[idx][i] == 1 and i not in good) or (statements[idx][i] == 0 and i in good) or (i in good and statements[i][idx] == 0):
                    break
            else:
				# if no contradiction found then we can assume idx is good and continue search
                solution_1479_3_2(idx + 1, count + 1)
            good.remove(idx)
            
            # assume idx is bad
            for i in range(idx):
				# check for any contradictions with previous candidates thought to be good
                if (i in good and statements[i][idx] == 1):
					# contradiction so prune current branch
                    return
            solution_1479_3_2(idx + 1, count)
    
        solution_1479_3_2(0, 0)
        return self.ans