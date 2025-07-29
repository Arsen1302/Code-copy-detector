class Solution:
    def solution_546_4(self, s: str, goal: str) -> bool:
        index =[]
        if len(s)==1:
            return False

        if s==goal and len(set(s))<len(s):
            return True;
        
        for i in range(len(s)):
            if s[i]!=goal[i]:
                index.append(i)
        
        if(len(index)!=2):
            return False;
        
        new_s = list(s)
        swap1 = new_s[index[0]]
        swap2 = new_s[index[1]]
        new_s[index[0]] = swap2
        new_s[index[1]] = swap1
        new_s = ''.join(new_s)
        
        if new_s==goal:
            return True
        else:
            return False