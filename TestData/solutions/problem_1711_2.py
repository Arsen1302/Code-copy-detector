class Solution:
    def solution_1711_2(self, nums: List[int], k: int) -> int:
        window = Counter(nums[:k])
        size = len(window)
        n = len(nums)
        running = sum(nums[:k])
        max_total = running if size == k else 0

        for i in range(k, n):
            out, v = nums[i-k], nums[i]
            window[out] -= 1
            if window[out] == 0:
                window.pop(out)
                size -= 1
            
            if v in window:
                window[v] += 1
            else:
                window[v] = 1
                size += 1
            
            running = running + v - out
            #print(f"{i}: {nums[i]}; {running} | {window}")
            if size == k and running > max_total:
                max_total = running

        return max_total