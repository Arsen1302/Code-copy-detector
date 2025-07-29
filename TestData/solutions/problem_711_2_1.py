class Solution:
    def solution_711_2_1(self,arr,size):
        n = len(arr)
        if n < size: return 0
        best = tmp = sum(arr[:size])
        for i in range(1,n-size+1):
            tmp = tmp + arr[i+size-1] - arr[i-1]
            if tmp > best:best = tmp
        return best
    def solution_711_2_2(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        summ = sum(nums[:firstLen])
        ans = summ  + self.solution_711_2_1(nums[firstLen:],secondLen)   
        for i in range(1,n-firstLen+1):
            summ = summ + nums[i+firstLen-1] - nums[i-1]
            a = self.solution_711_2_1(nums[:i],secondLen)
            b = self.solution_711_2_1(nums[i+firstLen:],secondLen)
            m = a if a > b else b
            if summ + m > ans: ans = summ + m
        return ans