class Solution:
    def solution_1445_5(self, st: str, sp: List[int]) -> str:
        ret = [st[:sp[0]]]  # writing the initial part of the string (from index 0 to the 1st space) to the variable
            
        for i in range(1, len(sp)):
		    # going throught each space
            ret.append(' ')  # adding space at the position
            ret.append(st[sp[i-1]:sp[i]])  # writing the next part of the string, which does not have spaces in between
            
        ret.append(' ')
        ret.append(st[sp[-1]:])  # writing the last part of string to the variable
        
        return ''.join(ret)  # converting the contents of list to string