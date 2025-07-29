class Solution:
    def solution_691_4_1(self, weights: List[int], days: int) -> int:
        
        def solution_691_4_2(kilos):
            neededDays=1
            shipmentSize=0
            for package in weights:
                if shipmentSize+package<=kilos:
                    shipmentSize+=package
                else:
                    shipmentSize=package
                    neededDays+=1
            return neededDays
        
		
        def solution_691_4_3(l,h):
            while l<h:
                kilos=(l+h)//2
                if solution_691_4_2(kilos)<=days:
                    h=kilos
                else:
                    l=kilos+1
            return l


        l=max(weights)
        h=sum(weights)
        return solution_691_4_3(l,h)