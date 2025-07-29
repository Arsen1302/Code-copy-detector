class Solution:
    def solution_802_4(self, arr: List[int], difference: int) -> int:
	
        myDict=Counter()
        
        for n in arr:
                myDict[n+difference]=myDict[n]+1 if n in myDict else 1
            
        return max(myDict.values())