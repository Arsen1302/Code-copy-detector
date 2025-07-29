class Solution:
    def solution_67_1_1(self, a: List[int]) -> int:
        
        def solution_67_1_2(l,h):
            while l<h:
                m=(l+h)//2
                
                if a[m]<a[m-1]:
                    return a[m]
                
                elif a[m]>a[h-1]:
                    l=m+1
                
                elif a[m]<a[h-1]:
                    h=m
                
                else:
                
                    if len(set(a[l:m+1]))==1:
                        return min(a[m],solution_67_1_2(m+1,h))
                    
                    else:
                        return min(a[m],solution_67_1_2(l,m))
            
            return a[min(l,len(a)-1)]
        
        return solution_67_1_2(0,len(a))