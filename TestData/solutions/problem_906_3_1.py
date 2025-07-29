class Solution:
    
    ALPHABET_LENGTH = 26
    ASCII_OFFSET = 97
    
    def solution_906_3_1(self, votes: List[str]) -> str:
        """
        1. Build array rank where rank[i][j] is the number of votes for team i to be the j-th rank.
        2. Sort the teams by rank array. if rank array is the same for two or more teams, sort them by the ID in ascending order.
        """        
        num_teams = len(votes[0])
        ranks = [[0 for i in range(self.ALPHABET_LENGTH)] for j in range(len(votes[0]))]
        
        # Populate Ranks Matrix
        for voter_index, vote in enumerate(votes):
            for rank, team in enumerate(vote):
                ranks[rank][self.solution_906_3_4(team)] = ranks[rank][self.solution_906_3_4(team)] + 1       
        
        # Associate Teams with their Votes (Columns)
        # Take care of sorting by appending duplicates to value list
        teams_to_ranks = {}
        for team, rankings in enumerate(self.solution_906_3_2(ranks)):
            tuple_key = tuple(rankings)
            if tuple_key in teams_to_ranks:
                teams_to_ranks[tuple_key].append(self.solution_906_3_3(team))
            else:
                teams_to_ranks[tuple_key] = [self.solution_906_3_3(team)]
        
        # Sort Teams (Columns) of Rank Matrix by Rank (Rows)
        ranks = self.solution_906_3_2(ranks)
        ranks.sort(key=lambda row: row[:], reverse=True)
        ranks = self.solution_906_3_2(ranks)
        
        # Assemble String of Final Rankings
        final_ranking = ""
        for team, rankings in enumerate(self.solution_906_3_2(ranks)):
            tuple_key = tuple(rankings)
            teams_with_rankings = teams_to_ranks[tuple_key] # Can't search transposed!
            
            if len(teams_with_rankings) > 1: # If multiple teams have the same rankings, get the first by alphabet
                sorted_ranking = sorted(teams_with_rankings)
                final_ranking += sorted_ranking.pop(0)
                teams_to_ranks[tuple_key] = sorted_ranking
            else: # Otherwise just append the team matched with that ranking
                final_ranking += teams_with_rankings[0]
    
        return final_ranking[:num_teams] # Everything behind num teams is extra
        
        
    def solution_906_3_2(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    def solution_906_3_3(self, position: int) -> str:
        return chr(position + self.ASCII_OFFSET).upper()
    
    def solution_906_3_4(self, char: str) -> int:
        return ord(char.lower()) - self.ASCII_OFFSET