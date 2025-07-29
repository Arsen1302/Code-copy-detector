class Solution:
    def solution_1468_1(self, s: str, k: int, fill: str) -> List[str]:
        length = len(s)
        res=[]
        for i in range(0,length,k):
            if i+k>length:
                break
            res.append(s[i:i+k])
        mod =length%k 
        
        if mod!= 0:
            fill_str = fill *(k-mod)
            add_str = s[i:]+fill_str
            res.append(add_str)
            
        return res