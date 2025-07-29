class Solution:
    def solution_658_5(self, nums: List[int]) -> List[int]:
        res = []
        num_deque = collections.deque(nums)

        while num_deque:
            left = num_deque[0] ** 2
            right = num_deque[-1] ** 2

            if left > right:
                res.append(left)
                num_deque.popleft()
            else:
                res.append(right)
                num_deque.pop()
        
        return res[::-1]