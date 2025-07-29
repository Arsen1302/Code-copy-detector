class Solution:
    def solution_1669_5_1(self, nums: List[int]) -> List[int]:
        def solution_1669_5_2(k):
            ret = []
            while k>0:
                ret.append(k%2)
                k = k // 2
            return ret
        
        n = len(nums)
        h = [[] for _ in range(32)]
        for i in range(n):
            bi = solution_1669_5_2(nums[i])
            for j in range(len(bi)):
                if bi[j]==1:
                    h[j].append(i)
                    
        print(nums)
        print("h:", {i:h[i] for i in range(len(h)) if len(h[i])>0})
        
        vt = [0 for _ in range(32)]
        lh = [len(h[i]) for i in range(32)] 
        ans = []
        for i in range(n):
            r = i
            for k in range(32):
                if vt[k]<lh[k] and h[k][vt[k]]<i:
                    vt[k] += 1
                if vt[k]<lh[k]:
                    r = max(r, h[k][vt[k]])
            
            print("+ ", i, r, "size:", r - i + 1, "h:", [h[i][vt[i]:] for i in range(len(h)) if len(h[i])>0])
            ans.append(r - i + 1)
        print("ans:", ans)
        print("="*20, "\n")
        return ans
		
print = lambda *a, **aa: ()