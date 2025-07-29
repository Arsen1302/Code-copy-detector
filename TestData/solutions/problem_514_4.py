class Solution:
    def solution_514_4(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = sorted(zip(difficulty, profit))
        ans = i = mx = 0 
        for w in sorted(worker): 
            while i < len(job) and job[i][0] <= w: 
                mx = max(mx, job[i][1])
                i += 1
            ans += mx 
        return ans