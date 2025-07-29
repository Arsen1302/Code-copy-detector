class Solution:
    def solution_622_5(self, arr: List[int]) -> bool:
        i=arr.index(max(arr))
        if arr.count(max(arr))>=2:
            return False
        lst1=arr[:i:]
        lst2=arr[i+1::]
        
        if (sorted(lst1)!=lst1 or sorted(lst2,reverse=True)!=lst2) or (len(lst1)==0 or len(lst2)==0) :
            return False
        dict1=collections.Counter(lst1)
        dict2=collections.Counter(lst2)
        for key,val in dict1.items():
            if val>=2:
                return False
        for key,val in dict2.items():
            if val>=2:
                return False
        return True