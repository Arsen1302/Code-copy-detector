class Solution:
    def solution_1373_3(self, nums: List[int]) -> int:
        
        answer = float("+inf")
        for i in range(len(nums)):
            minimum = nums[i]
            used = set()
            total = 0
            for j in range(len(nums)):
                if minimum <= nums[j] <= minimum + len(nums) - 1:
                    if nums[j] in used:
                        total += 1
                    else:
                        used.add(nums[j])
                else:
                    total += 1
            answer = min(answer, total)
            
        return answer