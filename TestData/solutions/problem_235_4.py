class Solution:
def solution_235_4(self, start: str, end: str, bank: List[str]) -> int:
    
    if end not in bank:
        return -1
    
    q = deque()
    q.append((start,0))
    while q:
        tochk,limit = q.popleft()
        if tochk == end:
            return limit
        
        w = 0
        while w<len(bank):
            word = bank[w]
            c = 0
            for i in range(8):
                if tochk[i]!=word[i]:
                    c+=1
            
			if c==1:
                q.append((word,limit+1))
                bank.remove(word)
                continue   
            w+=1
    
    return -1