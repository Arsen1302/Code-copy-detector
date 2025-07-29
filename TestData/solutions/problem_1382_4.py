class Solution:
    def solution_1382_4(self, nums: List[str], target: str) -> int:
        d = collections.defaultdict(int)
        
        for num in nums:
            d[num] += 1
        
        res = 0
        for num in nums:
            if len(num) < len(target) and num == target[:len(num)]:
                val = target[len(num):]
                val_cnt = d[target[len(num):]]
                if val == num:
                    val_cnt -= 1
                    
                res += val_cnt
        
        return res