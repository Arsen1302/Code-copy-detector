class Solution:
    def solution_153_4(self, nums: List[int]) -> List[int]:
        ans = []
        deque = collections.deque()
        for num in nums[::-1]:
            index = bisect.bisect_left(deque,num)
            ans.append(index)
            deque.insert(index,num)
        return ans[::-1]