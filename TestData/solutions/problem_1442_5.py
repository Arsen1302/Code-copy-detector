class Solution:
    def solution_1442_5(self, plants: List[int], capacityA: int, capacityB: int) -> int:  
        n=len(plants)
        if n==1:
            if capacityA>=plants[0] or capacityB>=plants[0]:
                return 0 
            else:
                return 1
        s=0
        pa=capacityA
        pb=capacityB
        length=n
        if n%2!=0:
            length=n+1
        for i in range(1,length//2):
            da=capacityA-plants[i-1]
            db=capacityB-plants[n-i]
            if i==n-i-1:
                if da>=plants[i] or db>=plants[i]:
                    return s 
                else:
                    return s+1 
            if da>=plants[i]:
                capacityA=da
            else:
                s+=1
                capacityA=pa
            if db>=plants[n-i-1]:
                capacityB=db
            else:
                s+=1
                capacityB=pb
        return s