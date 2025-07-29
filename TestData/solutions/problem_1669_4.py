class Solution:
    def solution_1669_4(self, nums: List[int]) -> List[int]:
        # store digits with 1 bit
        digits = defaultdict(lambda: defaultdict(int))

        for num in set(nums):
            if not num: continue
            d = bin(num)[2:]
            for i, x in enumerate(d[::-1]):
                if x == '1':
                    digits[num][i] += 1

        
        n = len(nums)
        r = n - 1
        ans = [0] * n
        tmp = defaultdict(int)
        for l in reversed(range(n)):
            for x in digits[nums[l]]:
                tmp[x] += 1
            
            # to be removed number will not cause current digits to have zero count after removal
            while r > l and all(tmp[x] > 1 for x in digits[nums[r]]):
                for x in digits[nums[r]]:
                    tmp[x] -= 1
                r -= 1

            ans[l] =  r - l + 1
        
        return ans