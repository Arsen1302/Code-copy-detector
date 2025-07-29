class Solution:
    def solution_1697_1_1(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK: return 0
        
        def solution_1697_1_2(l, r):
            if l + 1 == r: return 0
            dic = Counter([nums[l]])
            ans, j = 0, l + 1
            for i in range(l + 1, r):
                dic[nums[i - 1]] -= 1
                while not dic[minK] * dic[maxK] and j < r:
                    dic[nums[j]] += 1
                    j += 1
                if dic[minK] * dic[maxK]: ans += r - j + 1
                else: break
            return ans
        
        arr = [-1] + [i for i, num in enumerate(nums) if num < minK or num > maxK] + [len(nums)]
        return sum(solution_1697_1_2(arr[i - 1], arr[i]) for i in range(1, len(arr)))