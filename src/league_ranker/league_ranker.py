# Calculates league rankings based on match results
from typing import Dict, List, Tuple
from collections import defaultdict

class LeagueRanker:
    def __init__(self):
        self.team_points = defaultdict(int)
        
    def process_match(self, match_result: str) -> None:
        """ Process a single match result and update team points """
        try:
            team1_info, team2_info = [x.strip() for x in match_result.split(',')]
            
            team1_name = ' '.join(team1_info.split()[:-1])
            team1_score = int(team1_info.split()[-1])
            
            team2_name = ' '.join(team2_info.split()[:-1])
            team2_score = int(team2_info.split()[-1])
            
            # Validate scores
            if team1_score < 0 or team2_score < 0:
                raise ValueError("Invalid match result format: scores cannot be negative")
            
            if team1_score > team2_score:
                self.team_points[team1_name] += 3
                self.team_points[team2_name] += 0
            elif team1_score < team2_score:
                self.team_points[team1_name] += 0
                self.team_points[team2_name] += 3
            else:
                self.team_points[team1_name] += 1
                self.team_points[team2_name] += 1
                
        except (ValueError, IndexError) as e:
            raise ValueError(f"Invalid match result format: {match_result}")

    def get_rankings(self) -> List[Tuple[int, str, int]]:
        """ Calculate and return the rankings """
        if not self.team_points:
            return []
        
        # Sort teams by points (descending) and name (ascending)
        sorted_teams = sorted(
            self.team_points.items(),
            key=lambda x: (-x[1], x[0])
        )
        
        rankings = []
        current_rank = 1
        previous_points = None
        teams_at_current_points = 0
        
        for i, (team, points) in enumerate(sorted_teams):
            if previous_points != points:
                current_rank = i + 1
                teams_at_current_points = 1
                previous_points = points
            else:
                teams_at_current_points += 1
                
            rankings.append((current_rank, team, points))
            
        return rankings

    def process_input(self, input_data: str) -> str:
        """ Process multiple match results and return formatted rankings """
        if not input_data.strip():
            raise ValueError("Error: Input data is empty.")
            
        self.team_points.clear()
        
        for line in input_data.strip().split('\n'):
            if line.strip():
                self.process_match(line)
        
        rankings = self.get_rankings()
        output_lines = []
        
        for rank, team, points in rankings:
            points_text = "pt" if points == 1 else "pts"
            output_lines.append(f"{rank}. {team}, {points} {points_text}")
            
        return '\n'.join(output_lines)