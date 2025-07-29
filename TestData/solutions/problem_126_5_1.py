class Solution(object):
    def solution_126_5_1(self, expression):
       
        res=[]
        def solution_126_5_2(s,memo={}):
            res=[]
            if s in memo:
                return memo[s]
            if s.isdigit():
                return [int(s)] #if string containsonly numbers return that
            syms=['-','+','*','/']
            for i in range(len(s)):
                symbol=s[i]
                if s[i] in syms: #if the character is a operator
                    left=solution_126_5_2(s[:i],memo) #possible values from left
                    right=solution_126_5_2(s[i+1:],memo) #possible values from right
                    for l in left:         #Using nested for loops, calculate all possible combinations of left and right values applying exp[i] operator
                        for r in right:
                            if symbol=='+':
                                res.append(l+r)
                            elif symbol=='-':
                                res.append(l-r)
                            elif symbol=='*':
                                res.append(l*r)
                            else:
                                res.append(l//r)
            memo[s]=res
            return res
        return solution_126_5_2(expression)