class Solution:
    def solution_1442_4(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        # check whether they will reach the same plant (uneven array length)
        same_plant = len(plants) % 2 == 1
        
        # get the middle plant
        mid_plant = len(plants)//2
        
        # make the two buckets
        a_bucket = capacityA
        b_bucket = capacityB
        fillups = 0
        for idx in range(mid_plant):
            # check alice
            if a_bucket >= plants[idx]:
                a_bucket -= plants[idx]
            else:
                fillups += 1
                a_bucket = capacityA - plants[idx]
            
            # check bob
            if b_bucket >= plants[-idx-1]:
                b_bucket -= plants[-idx-1]
            else:
                fillups += 1
                b_bucket = capacityB - plants[-idx-1]
        
        # check whether we meet at the same place and need to refill there
        leftover_plant = plants[mid_plant]
        if same_plant and a_bucket < leftover_plant and b_bucket < leftover_plant:
            fillups += 1
            
        return fillups