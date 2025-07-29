class Solution:
    def solution_589_4(self, nums: List[int]) -> List[int]:
        l = deque([])
        for i in nums:
            if i % 2:
                l.append(i)
            else:
                l.appendleft(i)
        return l