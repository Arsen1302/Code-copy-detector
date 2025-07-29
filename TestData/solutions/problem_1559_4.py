class Solution:
    def solution_1559_4(self, nums: List[int], k: int, p: int) -> int:
        trie = {}
        cnt = 0
        for i in range(len(nums)):
            count = 0
            divis = 0    #contain count of element in array divisible by p
            d = trie
            for j in range(i,len(nums)):
                if nums[j] % p == 0:
                    divis += 1
                if divis > k:
                    break
                if nums[j] not in d:
                    d[nums[j]] = {}
                    count += 1
                d = d[nums[j]]
            cnt += count   #count contain all subarrays that can be made from nums[i:j]
        return cnt```