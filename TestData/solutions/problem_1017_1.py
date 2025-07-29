class Solution:
    def solution_1017_1(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for number in nums:            
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1
        return res