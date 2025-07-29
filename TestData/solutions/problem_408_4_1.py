class Solution:
       def solution_408_4_1(self, stickers: List[str], target: str) -> int:
            tf={}
            for c in target:
                if c not in tf:
                    tf[c]=0
                tf[c]+=1
            w2f={}
            for word in stickers:
                w2f[word]={}
                for c in word:
                    if c in tf:
                        if c not in w2f[word]:
                            w2f[word][c]=0
                        w2f[word][c]+=1
            res=float('inf')
            ## remove dominated words
            def solution_408_4_2(a,b):
                for c in w2f[b]:
                    if c in w2f[a] and w2f[a][c]>=w2f[b][c]:
                        continue
                    else:
                        return False
                return True
            for w in stickers:
                if w not in w2f:continue
                for w2 in stickers:
                    if w2!=w and w2 in w2f and solution_408_4_2(w2,w):
                        del w2f[w]
                        break

            def solution_408_4_3(ct, charhas, i):
                nonlocal res
                if ct>=res: return
                if i==len(target):
                    res=min(res,ct)
                    return 
                ch=target[i]
                if charhas[ch]>0:
                    charhas[ch]-=1
                    solution_408_4_3(ct,charhas,i+1)
                    charhas[ch]+=1
                else:
                    for w in w2f:
                        if ch not in w:continue 
                        for c in w2f[w]:
                            charhas[c]+=w2f[w][c]
                        solution_408_4_3(ct+1,charhas,i)
                        for c in w2f[w]:
                            charhas[c]-=w2f[w][c]
                return
            solution_408_4_3(0,defaultdict(int),0)
            return res if res<float('inf') else -1