# League Ranking Calculator

# Overview
A production-grade command-line application for calculating league rankings based on game results.
The ranking is based on wins, draws, and losses from the input match results.

# Features
Calculates team rankings based on match results.
Awards 3 points for a win, 1 point for a draw, and 0 points for a loss.
Handles ties in points by sorting teams alphabetically.
Outputs the rankings from highest to lowest
Accepts input from both files and standard input
Includes comprehensive test suite

# Requirements
- Python 3.6 or higher
- pytest (for running tests)
- Docker (optional)

# Installation
1. Clone the repository
- git clone git@github.com:yandisakat/league_ranker.git
- cd league-ranker

2. Create a virtual environment (optional but recommended):
- python -m venv venv
- source venv/bin/activate

3. Install dependencies
- pip install -r requirements.txt

# Docker Installation and Testing
1. Build the Docker image:
- docker build -t league_ranker_app .

2. Running with standard input:
- docker run -it --rm league_ranker_app
Then type or paste your input and press Ctrl+D (Unix) when finished.

3. Running automated tests in the Docker container:
- docker run --rm league_ranker_app pytest tests/ -v

# Local Usage
1. Reading from a file (run in file directory):
- python main.py input.txt

2. Reading from standard input (run in file directory):
- python main.py
Then type or paste your input and press Ctrl+D (Unix) when finished.

# Input Format
Each line should contain a match result in the following format:
- Team1Name Score1, Team2Name Score2

# Example:
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0

# Output Format
The output will be ordered from most to least points, with teams having the same points sharing the same rank and being listed in alphabetical order.

Example:
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts

# Running Tests
To run the tests:
- pytest tests/