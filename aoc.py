import argparse
import importlib
import os

def load_input(year, day):
    input_path = f"inputs/year_{year}/day{day}.txt"
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} not found.")
    with open(input_path, 'r') as file:
        return file.read().strip()

def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("year", type=int, help="Year of the solution (e.g., 2024)")
    parser.add_argument("day", type=int, help="Day of the solution (e.g., 1)")
    parser.add_argument("part", type=int, choices=[1, 2], help="Part of the solution (1 or 2)")
    args = parser.parse_args()

    try:
        # Dynamically import the solution module
        module_path = f"solutions.year_{args.year}.day{args.day}"
        solution_module = importlib.import_module(module_path)

        # Ensure part function exists
        part_function_name = f"part{args.part}"
        if not hasattr(solution_module, part_function_name):
            raise AttributeError(f"Solution for part {args.part} is not implemented.")

        # Load input and run the solution
        input_data = load_input(args.year, args.day)
        part_function = getattr(solution_module, part_function_name)
        result = part_function(input_data)
        print(f"Year {args.year}, Day {args.day}, Part {args.part}: {result}")

    except (ImportError, FileNotFoundError, AttributeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
