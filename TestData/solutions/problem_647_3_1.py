class Solution:
    def solution_647_3_1(self, wordlist: List[str], queries: List[str]) -> List[str]:
        low_origin, wild_origin = collections.defaultdict(str), collections.defaultdict(str)
        s = set(wordlist)            
        def solution_647_3_2(word): return ''.join(['*' if c in 'aeiou' else c for c in word])
        
        for word in wordlist:
            low = word.lower()
            if low not in low_origin: low_origin[low] = word
            wild = solution_647_3_2(low)
            if wild not in wild_origin: wild_origin[wild] = word
            
        ans = []
        for query in queries:
            low = query.lower()
            wild = solution_647_3_2(low)
            if query in s: ans.append(query)
            elif low in low_origin: ans.append(low_origin[low])    
            elif wild in wild_origin: ans.append(wild_origin[wild]) 
            else: ans.append('')
        return ans