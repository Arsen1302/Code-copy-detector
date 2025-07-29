class Solution:
    def solution_204_5(self, data: List[int]) -> bool:
        l = []
        
        for i in range(len(data)):
            l.append(bin(data[i])[2:])
            if(len(l[i]) < 8):
                l[i] = '0'*(8-len(l[i]))+l[i]
        curr = 0
        byte = 0
        flag = True
        for i in range(len(l)):
            if(byte == 0):
                j = 0
                while(j < len(l[i]) and l[i][j] == '1'):
                    byte +=1
                    j += 1
                flag = True
            elif(byte > 0):
                if(flag):
                    byte -= 1
                    flag = False
                if l[i][:2] != '10':
                    return False
                byte -= 1
            if byte > 4:
                return False
        if(byte > 0 and len(l) == 1):
            return False
        if(byte > 0):
            return False
        return True