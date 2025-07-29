class Solution:
    def solution_315_5_1(self, nums: List[int], k: int) -> int:
        return self.solution_315_5_2(nums, k)
    
    
    def solution_315_5_2(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        res = 0
        for i in c:
            if (k > 0 and (i + k) in c) or (k == 0 and c[i] > 1):
                res += 1
        return res
    
    
   # This is Idea but 1 2 testcases are not working 
    def solution_315_5_3(self, nums: List[int], k: int) -> int:
        pair = 0
        pairset = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k and (nums[i], nums[j]) not in pairset and (nums[j], nums[i]) not in pairset:
                    print(nums[i], nums[j])
                    pairset.add((nums[i], nums[j]))
                    pair += 1
        
        return pair