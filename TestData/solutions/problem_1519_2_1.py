class Solution:
    def solution_1519_2_1(self, text: str, pattern: str) -> int:
        
        # Logic:
        # I am sure if I filter letters of pattern, I can accomplish my task.
        # I am sure if I append the first letter of the pattern in the filtered string,
        # at the beginning and the second letter of the pattern at the end, I can get the maximum
        # number subsequences which is the pattern.
        # I need to count the occurrance of pattern[0] and pattern[1]
        #After I filtered, The only letters in string are pattern[0] and pattern[1]
        #let_ONE=0 #The maximum number of subsequence up to the current index
        #let_TWO=0 # The second letter counter==pattern[1]
        
        filtered=[]
        for let in text:
            if let  in pattern:
                filtered.append(let)
        return  max(self.solution_1519_2_2(False,filtered,pattern),
                    self.solution_1519_2_2(True,filtered,pattern))
        
        
    def solution_1519_2_2(self,atTheBeginning,string,pattern):
        
        let_ONE=0 
        let_TWO=0
        if not atTheBeginning:
            let_TWO=1
        for index in range(len(string)-1,-1,-1):
            if string[index]==pattern[0]:
                let_ONE+=let_TWO
            if string[index]==pattern[1]:
                let_TWO+=1
        if atTheBeginning:
            let_ONE+=let_TWO
        return let_ONE