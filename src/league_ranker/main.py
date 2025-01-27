# Command-line app for calculating league rankings
import sys
import os
import argparse
from league_ranker import LeagueRanker

def read_input_from_stdin():
    """ Reads input from stdin if no file is provided """
    print("Please enter match results (press Ctrl+D when finished):")
    return sys.stdin.read()

def read_input_from_file(file_path):
    """ Reads input from a file """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Error: Could not find file '{file_path}'")
    
    with open(file_path, 'r') as file:
        return file.read()

def process_input(input_data):
    """ Processes the input using LeagueRanker """
    if not input_data.strip():
        raise ValueError("Error: Input data is empty.")
    
    calculator = LeagueRanker()
    return calculator.process_input(input_data)

def main():
    parser = argparse.ArgumentParser(description="Process league match results and display rankings.")
    parser.add_argument('file', nargs='?', help='Path to the file containing match results (optional)')
    
    args = parser.parse_args()
    
    try:
        # Read input from file or stdin
        if args.file:
            input_data = read_input_from_file(args.file)
        else:
            input_data = read_input_from_stdin()
        
        # Process input and print rankings
        output = process_input(input_data)
        print(output)
    
    except FileNotFoundError as e:
        print(e)
        sys.exit(2)  # Specific exit code for file not found
    except ValueError as e:
        print(e)
        sys.exit(3)  # Specific exit code for invalid input
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)  # General exit code for other errors

if __name__ == "__main__":
    main()