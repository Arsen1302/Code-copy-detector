class Solution:
    def solution_229_2_1(self, nums: List[int]) -> int:
        def solution_229_2_2(group0=[], group1=[], div_bit=0):
            if len(group0) + len(group1) <= 1: return 0
            if len(group0) == 1 and len(group1) == 1: return group0[0] ^ group1[0]
            if div_bit == -1 and group0 and group1: return group0[0] ^ group1[0]
            if div_bit == -1: return 0
            nbit = div_bit - 1
            
            if group0 and group1:
                group00, group01 = solution_229_2_3(group0, div_bit)
                group10, group11 = solution_229_2_3(group1, div_bit)
                if (group00 and group11) and (group01 and group10):
                    return max(solution_229_2_2(group00, group11, nbit), solution_229_2_2(group10, group01, nbit))
                elif group00 and group11:
                    return solution_229_2_2(group00, group11, nbit)
                elif group01 and group10:
                    return solution_229_2_2(group10, group01, nbit)
                else:
                    return solution_229_2_2(group00 or group01, group10 or group11, nbit)
            else:
                group0, group1 = solution_229_2_3(group0 or group1, div_bit)
                return solution_229_2_2(group0, group1, nbit)
                
        max_num = max(nums)
        max_bit = int(math.log(max_num, 2)) if max_num else 0
        return solution_229_2_2(nums, [], max_bit)
        

def solution_229_2_3(nums, bit):
    mask = 1 << bit
    g0, g1 = [], []
    for num in nums:
        if num &amp; mask == 0:
            g0.append(num)
        else:
            g1.append(num)
    return g0, g1