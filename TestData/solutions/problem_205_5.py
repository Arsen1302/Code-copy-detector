class Solution:
    def solution_205_5(self, s: str) -> str:
                
        st = []
        
        for c in s:

            if c != ']':
                st.append(c)
            else:
				# join the string inside the 1st balanced brackets
                tmp = ""
                while st and st[-1] != '[':                                        
                    tmp = st.pop() + tmp
                
				# pop out the opening `[`
                st.pop()
                num = ""
				
				# calculate the multiplier
                while st and st[-1].isdigit():
                    num = st.pop() + num
                    
                # add the multiplied string back to the stack
                st.append(int(num)*tmp)
        
        return ''.join(st)