class Solution:
    def solution_937_4(self, s: str) -> int:
        if s == '1': return 0
        
        s = [a for a in str(s)]
        count = 0
        
        # print(s)
        while 1 < len(s):
            if s[-1] == '1':
                # add 1
                s[-1] = '0'
                carry = True
                # check from the end if need to carry forward
                # or the carry can be 'absorb' by a zero
                for i in range(len(s) - 2, -1, -1):
                    if carry == True:
                        if s[i] == '1':    
                            s[i] = '0'
                            carry = True
                        else:
                            s[i] = '1'
                            carry = False
                            break
                # if there is still carry at the end
                # prepend a '1' at the beginning
                if carry:
                    s.insert(0, '1')
            else:
                # divide it by 2
                s = s[:-1]
            count += 1
            # print(s)
        
        if s == ['0']: return null
        return count