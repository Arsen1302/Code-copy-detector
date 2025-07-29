class Solution:
    def solution_1455_5_1(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        def solution_1455_5_2(k):
            cnt = defaultdict(int)
            ans = []
            for x in nums:
                if cnt[x - 2*k] > 0:
                    cnt[x - 2*k] -= 1
                    ans.append(x - k)
                else:
                    cnt[x] += 1
            if len(ans) == n // 2: return ans
            return []
                       
	    # maximum k should not exceed half of the array
        cand_k = sorted(set((nums[i] - nums[0]) // 2 for i in range(1, n // 2 + 1) if (nums[i] - nums[0]) % 2 == 0))
        for k in cand_k:
            if k == 0: continue
            ans = solution_1455_5_2(k)
            if ans: return ans