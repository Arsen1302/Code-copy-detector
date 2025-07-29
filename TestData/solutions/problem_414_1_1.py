class Solution:
    def solution_414_1_1(self, nums: List[int], k: int) -> bool:
        if k==1:
            return True
        total = sum(nums)
        n = len(nums)
        if total%k!=0:
            return False
        nums.sort(reverse=True)
        average = total//k
        if nums[0]>average:
            return False
        
        visited = [False]*n
        def solution_414_1_2(cur, begin, k):
            if k==0:
                return True
            if cur>average:
                return False
            elif cur==average:
                return solution_414_1_2(0, 0, k-1)
            for i in range(begin, n):
                if not visited[i]:
                    visited[i] = True
                    if solution_414_1_2(cur + nums[i], i+1, k):
                        return True
                    visited[i] = False
            return False
        
        return solution_414_1_2(0, 0, k)