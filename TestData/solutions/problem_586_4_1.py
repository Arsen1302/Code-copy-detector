class Solution:
    def solution_586_4_1 (self, digits, n):
        cnt = 0
        for i in range (1, len(str(n))):
            cnt += len(digits)** i
        return cnt
    
    def solution_586_4_2 (self, digits, n):
        s = str(n)
        cnt = 0 
        for i in range (len(s)):
            valid_digits_counter = 0
            for d in digits:
                if d < s[i]:
                    valid_digits_counter+=1
            cnt+= valid_digits_counter * (len(digits)**(len(s)-i-1))
            if s[i] not in digits:
                break
            cnt+=1 if i==len(s)-1 else 0
        return cnt
                    
            
    def solution_586_4_3(self, digits: List[str], n: int) -> int:
        return self.solution_586_4_1(digits, n) + self.solution_586_4_2(digits,n)