# Test suite for the League Ranker application.
import pytest
from src.league_ranker.league_ranker import LeagueRanker

@pytest.fixture
def ranker():
    return LeagueRanker()

def test_process_single_match():
    ranker = LeagueRanker()
    ranker.process_match("Lions 3, Snakes 3")
    assert ranker.team_points["Lions"] == 1
    assert ranker.team_points["Snakes"] == 1

def test_process_multiple_matches():
    ranker = LeagueRanker()
    input_data = """Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1"""
    output = ranker.process_input(input_data)
    expected = """1. Tarantulas, 6 pts
2. Lions, 2 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt"""
    assert output.strip() == expected.strip()

def test_invalid_match_format():
    ranker = LeagueRanker()
    with pytest.raises(ValueError):
        ranker.process_match("Invalid Format")

def test_empty_input():
    ranker = LeagueRanker()
    with pytest.raises(ValueError):
        ranker.process_input("")

def test_tied_teams_alphabetical_order():
    ranker = LeagueRanker()
    input_data = """AAA Team 1, BBB Team 0
CCC Team 1, BBB Team 0"""
    output = ranker.process_input(input_data)
    expected = """1. AAA Team, 3 pts
1. CCC Team, 3 pts
3. BBB Team, 0 pts"""
    assert output.strip() == expected.strip()

def test_sample_input():
    calc = LeagueRanker()
    sample_input = """Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0"""
    
    expected_output = """1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts"""
    
    assert calc.process_input(sample_input) == expected_output

def test_whitespace_handling():
    ranker = LeagueRanker()
    input_data = "  Lions   3  ,   Snakes    3  "
    ranker.process_match(input_data)
    assert ranker.team_points["Lions"] == 1
    assert ranker.team_points["Snakes"] == 1

def test_team_names_with_spaces():
    ranker = LeagueRanker()
    ranker.process_match("FC Awesome 3, Real Madrid 3")
    assert ranker.team_points["FC Awesome"] == 1
    assert ranker.team_points["Real Madrid"] == 1

def test_negative_scores():
    ranker = LeagueRanker()
    with pytest.raises(ValueError) as exc_info:
        ranker.process_match("Team A -1, Team B 0")
    assert "Invalid match result format" in str(exc_info.value)

def test_score_validation():
    ranker = LeagueRanker()
    # Test negative scores
    with pytest.raises(ValueError):
        ranker.process_match("Team A -1, Team B 0")
    # Test non-integer scores
    with pytest.raises(ValueError):
        ranker.process_match("Team A 1.5, Team B 2")
    # Test non-numeric scores
    with pytest.raises(ValueError):
        ranker.process_match("Team A abc, Team B 2")