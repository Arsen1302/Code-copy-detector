class Solution:
    def solution_1069_1_1(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        def solution_1069_1_2(x: int) -> List[int]:
            """
            Returns friends of x that have a higher preference than partner.
            """
			partner = partners[x]  # Find the partner of x.
            x_friends = friend_prefs[x]  # Find all the friends of x.
            partner_ranking = x_friends[partner]  # Get the partner's ranking amongst those friends.
            return list(x_friends)[:partner_ranking]  # Return all friends with a preferred lower ranking.

        def solution_1069_1_3(x: int) -> bool:
            """
            Returns True if person x is unhappy, otherwise False.
            """
            # Find the partner for person x.
            partner = partners[x]  
            # Find the friends that person x prefers more than this partner.
            preferred_friends = solution_1069_1_2(x)  
            # A friend is unhappy with their partner if there is another friend with a higher preference 
            # and that friend prefers them over their partner.
            return any(friend_prefs[friend][x] <= friend_prefs[friend][partners[friend]] 
                       for friend in preferred_friends)

        # Create dictionary to lookup friend preference for any person.
        friend_prefs = {
            person: {friend: pref for pref, friend in enumerate(friends)}
            for person, friends in enumerate(preferences)
        }
		# Example:
		# {0: {1: 0, 3: 1, 2: 2},
	    #  1: {2: 0, 3: 1, 0: 2},
	    #  2: {1: 0, 3: 1, 0: 2},
	    #  3: {0: 0, 2: 1, 1: 2}}
 
        # Create dictionary to find anyone's partner.
        partners = {}
        for x, y in pairs:
            partners[x] = y
            partners[y] = x
        
		# Count and return the number of unhappy people.
        return sum(solution_1069_1_3(person) for person in range(n))