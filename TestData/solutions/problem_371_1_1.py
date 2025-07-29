class Solution:
    def solution_371_1_1(self, equation: str) -> str:
        def solution_371_1_2(l,r): # left inclusive and right exclusive
            constant = unknown = 0
            sign,val = 1,''
            while l < r:
                if equation[l].isnumeric():
                    val += equation[l]
                elif equation[l] == 'x':
                    unknown += sign*int(val or '1') # in case the coefficient is 1
                    val = ''
                else: # meet a +/-
                    if val:
                        constant += sign*int(val)
                    sign = 1 if equation[l]=='+' else -1
                    val = ''
                l += 1
            if val: # if the last digit is a number
                constant += sign*i
            return constant,unknown
    
        mid = equation.find('=')
        constant1,unknown1 = solution_371_1_2(0,mid)
        constant2,unknown2 = solution_371_1_2(mid+1,len(equation))
        const,var = constant2-constant1,unknown1-unknown2
        # print(a,b)
        if var == 0:
            if const == 0: return "Infinite solutions"
            else: return "No solution"
        else: return 'x={}'.format(const//var)