class Solution:
    def solution_774_2_1(self, text: str) -> int:
        freq = {}
        for ch in text:
            freq[ch] = freq.get(ch, 0)+1
        
        n=len(text)
        i=0
        distinct = 0
        cur={}
        def solution_774_2_2(ind):
            nonlocal distinct
            ch = text[ind]
            cur[ch] = cur.get(ch,0)+1
            if cur[ch] == 1:
                distinct+=1 
        def solution_774_2_3(ind):
            nonlocal distinct
            ch = text[ind]
            cur[ch]-=1
            if cur[ch]==0:
                cur.pop(ch)
                distinct-=1
        for j in range(n):
            #expansion
            solution_774_2_2(j)

            if distinct >= 3:
                #movement
                solution_774_2_3(i)
                i+=1
                continue
            if distinct == 2:
                keys = list(cur.keys())
                a,b = keys[0], keys[1]
                if cur[a] == 1 or cur[b] == 1:
                    if cur[a] == 1:
                        if freq[b] == cur[b]:
                            solution_774_2_3(i)
                            i+=1
                    else:
                        if freq[a] == cur[a]:
                            solution_774_2_3(i)
                            i+=1
                else:
                    solution_774_2_3(i)
                    i+=1
        return n-i