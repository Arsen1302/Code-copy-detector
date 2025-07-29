class Solution:
    def solution_972_1(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0 # If a value meets the criteria, one will be added here.

        for x, y in zip(startTime, endTime): # Zipping the two lists to allow us to iterate over them using x,y as our variables.
            if x <= queryTime <= y: # Checking if the queryTime number is between startTime and endTime, adding one to count if it is.
                    count += 1
        return count # Returning the value in count