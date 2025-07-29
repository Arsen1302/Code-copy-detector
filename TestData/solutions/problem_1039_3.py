class Solution:
    def solution_1039_3(self, s: str) -> int:
        stk = list()
        res = 0
        idx = 0
        while (idx < len(s)):
            c = s[idx]
            if (c == '('):
                stk.append(c)
            else: # 如果是right paren
                # Fill in left parenthesis
                if (not stk): # 如果没有left paren在stack
                    res += 1 
                    stk.append('(')
                
                # Paired right parenthesis.
                if (idx < len(s) - 1 and s[idx + 1] == ')'):
                    idx += 1
                    stk.pop()
                
                # Unpaired right parenthesis.
                else:
                    res += 1
                    stk.pop()
            
            idx += 1
        
        # Calculate unpaired left parenthesis.
        res += len(stk) * 2
        return res
        
        # # res 记录插入次数
        # # need 变量记录右括号的需求量
        # need, res = 0, 0

        # for i in range(len(s)):
        #     if s[i] == '(':
        #         need += 2
        #         # 当遇到左括号时，若对右括号的需求量为奇数，需要插入 1 个右括号。
        #         # 因为一个左括号需要两个右括号嘛，右括号的需求必须是偶数
        #         if need %2 == 1:
        #             # 插入一个右括号
        #             res += 1
        #             # 对右括号的需求减一
        #             need -= 1

        #     elif s[i] == ')':
        #         need -= 1
        #         # 说明右括号太多了
        #         if need == -1:
        #             # 需要插入一个左括号
        #             res += 1
        #             # 同时，对右括号的需求变为 1
        #             # -1 -> 1 # 相当于是add 2 to need
        #             need = 1
        # return need + res