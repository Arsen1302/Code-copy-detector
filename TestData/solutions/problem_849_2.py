class Solution:
    def solution_849_2(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False


        count = collections.Counter(nums)
        count = dict(sorted(count.items()))
        print(count)
        while count:
            start_key = list(count.keys())[0]
            count[start_key] -=1
            if count[start_key] == 0:
                count.pop(start_key)
            for i in range(1, k):
                if start_key + i not in count:
                    return False
                count[start_key+i] -=1
                if count[start_key+i] == 0:
                    count.pop(start_key+i)
        return True