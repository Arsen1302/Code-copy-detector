class Solution:
    def solution_329_4(self, n: int) -> int:
        num = list(str(n))

        i = len(num) - 1
        while i >= 1 and num[i] <= num[i - 1]:
            i -= 1
        
        if i == 0:
            return -1
        
        prefix = num[:i - 1]
        suffix = num[i - 1:]

        new_head_index = 0
        for i in range(1, len(suffix)):
            if int(suffix[i]) > int(suffix[0]):
                new_head_index += 1
            else:
                break
        # for i, n in enumerate(suffix):
        #     if int(n) > int(suffix[0]):
        #         new_head = min(new_head, int(n))
            
        # suffix.remove(str(new_head))
        # suffix = str(new_head) + "".join(sorted(suffix))

        suffix[0], suffix[new_head_index] = suffix[new_head_index], suffix[0]
        suffix = str(suffix[0]) + "".join(suffix[1:][::-1])

        ans = int("".join(prefix) + suffix)
        upper_bound = 2 ** 31 - 1
        return ans if ans <= upper_bound else -1
        
        

        # def helper(num):
        #     is_descending = True
        #     for i in range(len(num) - 1):
        #         if num[i] < num[i + 1]:
        #             is_descending = False
        #             break
                
        #     if is_descending:
        #         return -1
            
        #     suffix = helper(num[1:])
        #     if suffix == -1:
        #         new_head = 10
        #         for n in num[1:]:
        #             if int(n) > int(num[0]):
        #                 new_head = min(new_head, int(n))
                
        #         num.remove(str(new_head))
        #         return "".join([str(new_head)] + sorted(num))
            
        #     return num[0] + str(suffix)

        
        # ans = int(helper(num))
        # upper_bound = 2 ** 31 - 1
        # return ans if ans <= upper_bound else -1