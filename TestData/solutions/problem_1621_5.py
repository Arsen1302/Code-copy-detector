class Solution:
    def solution_1621_5(self, ranks: List[int], suits: List[str]) -> str:
        if(len(set(suits))==1):
            return "Flush"
        
        mp={}
        
        for i in range(5):
            if(ranks[i] not in mp):
                mp[ranks[i]]=1
            else:
                mp[ranks[i]]+=1
        
        for val in mp:
            if(mp[val]>=3):
                return "Three of a Kind"
            elif(mp[val]==2):
                return "Pair"
        
        return "High Card"