class Solution:
    def solution_1396_4(self, s: str) -> bool:
        
        nums = re.findall('\d+', s)
        nums = [int(num) for num in nums]
        
        if nums == sorted(nums) and len(nums) == len(set(nums)):
            return True
        else:
            return False