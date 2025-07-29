class Solution:
    def solution_316_5(self, num1: str, num2: str) -> str:
        num1_real, num1_comp = num1.split('+')
        num2_real, num2_comp = num2.split('+')
        
        # print(num1_real, num1_comp)
        # print(num2_real, num2_comp)
        if num1_comp[0] == '-' : 
            num1_comp_num = -1*int(num1_comp[1:-1])
        else : 
            num1_comp_num = int(num1_comp[:-1])
            
        if num2_comp[0] == '-' :
            num2_comp_num = -1*int(num2_comp[1:-1])
        else : 
            num2_comp_num = int(num2_comp[:-1])
            
        # print(num1_comp_num)
        # print(num2_comp_num)
        real_part = int(num1_real) * int(num2_real)
        real_part_comp = -1*(num2_comp_num * num1_comp_num)
        
        comp_part = (int(num1_real) * num2_comp_num) + (int(num2_real) * num1_comp_num)
        

        output = real_part + real_part_comp 

        output = str(output) + "+"+str(comp_part)+'i'
            
        return output