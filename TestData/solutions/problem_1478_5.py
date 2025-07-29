class Solution:
    def solution_1478_5(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        result = []
        for num in nums:
            if not count.get(num-1) and not count.get(num+1) and count.get(num, 0) < 2:
                result.append(num)
        return result