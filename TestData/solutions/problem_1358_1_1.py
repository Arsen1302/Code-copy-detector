class Solution:
    def solution_1358_1_1(self, tasks: List[int], sessionTime: int) -> int:
        subsets = []
        self.ans = len(tasks)
        
        def solution_1358_1_2(idx):
            if len(subsets) >= self.ans:
                return
            
            if idx == len(tasks):
                self.ans = min(self.ans, len(subsets))
                return
            
            for i in range(len(subsets)):
                if subsets[i] + tasks[idx] <= sessionTime:
                    subsets[i] += tasks[idx]
                    solution_1358_1_2(idx + 1)
                    subsets[i] -= tasks[idx]
            
            subsets.append(tasks[idx])
            solution_1358_1_2(idx + 1)
            subsets.pop()
        
        solution_1358_1_2(0)
        return self.ans