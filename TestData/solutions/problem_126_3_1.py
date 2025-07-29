class Solution:
    def solution_126_3_1(self, expression: str) -> List[int]:
        nums = '0123456789'
        
        def solution_126_3_2(a, b, c):
            if c == '+':
                return a + b
            elif c == '-':
                return a - b
            else:
                return a * b
        
        @lru_cache(None)
        def solution_126_3_3(l, r):
            if l == r:
                return [expression[l]]
            elif l > r:
                return []
            
            this = []
            went = 0
            for i in range(l, r + 1):
                if expression[i] not in nums:
                    went = 1
                    left = solution_126_3_3(l, i - 1)
                    right = solution_126_3_3(i + 1, r)
                    for leftvals in left:
                        for rightvals in right:
                            temp = solution_126_3_2(int(leftvals), int(rightvals), expression[i])
                            #print(temp)
                            this.append(temp)
            
            if went:
                return this
            else:
                return [expression[l: r + 1]]
        
        arr = solution_126_3_3(0, len(expression) - 1)
        #print(arr)
        return arr