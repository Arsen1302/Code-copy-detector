class Solution:
    def solution_1258_2_1(self, s: str) -> bool:
        s = str(int(s))
        def solution_1258_2_2(l):
            if len(l)<2:
                return False 
            #print(l)
            for i in range(len(l)-1):
                if int(l[i])!=int(l[i+1])+1:
                    return False
            return True
        
        def solution_1258_2_3(start,t,s):
            if start==len(s):
                if solution_1258_2_2(t):
                    return True
            for i in range(start,len(s)):
                if len(s[start:i+1])>1 and len(s[i+1:])>1 and int(s[start:i+1])<int(s[i+1:i+len(s[start:i+1])]):
                    continue
                if len(t)>1 and int(t[-1])<int(s[start:i+1]):
                    return
                t.append(s[start:i+1])
                if solution_1258_2_3(i+1,t,s):
                    return True
                t.pop()
                
            return False    
        return solution_1258_2_3(0,[],s)