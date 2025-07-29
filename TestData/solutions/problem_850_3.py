class Solution:
    def solution_850_3(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        md=Counter()
        l=0
        ans=Counter()
        for ind,ch in enumerate(s):
            md[ch]+=1
            while len(md.keys())>maxLetters:
                md[s[l]]-=1
                if not md[s[l]]:md.pop(s[l])
                l+=1
            for j in range(l,ind+1):
                if minSize<=ind-j+1<=maxSize:ans[s[j:ind+1]]+=1
        return max(ans.values()) if ans else 0