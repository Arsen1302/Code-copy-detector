class Solution:
    def solution_1039_4(self, s: str) -> int:
        insertion_num, right_need = 0, 0
        
        for i in range(len(s)):
            if (s[i] == '('):
                right_need += 2
                if (right_need % 2 == 1):
                    # we insert a right bracket
                    right_need -= 1
                    insertion_num += 1
                
            if(s[i] == ')'):
                right_need -= 1
                if (right_need == -1):
                    # we insert a left bracket
                    right_need += 2
                    insertion_num += 1
        
        return insertion_num + right_need