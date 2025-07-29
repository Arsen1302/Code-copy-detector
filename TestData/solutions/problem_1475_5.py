class Solution:
    def solution_1475_5(self, corridor: str) -> int:

        # go through the corridor and count seats
        # after that check whether there are plants
        # and we have several places to divide

        # go through the chairs and count
        chairs = 0
        positions = 1
        plants = 1
        for idx, element in enumerate(corridor):

            # check if we reached two chairs
            if chairs > 0 and chairs % 2 == 0:

                # check if current element is plant
                if element == 'S':
                    positions *= plants
                    plants = 1
                
                elif element == 'P':
                    plants += 1

            # count the chairs
            if element == 'S':
                chairs += 1
        return (positions % 1_000_000_007) if chairs > 0 and chairs % 2 == 0 else 0