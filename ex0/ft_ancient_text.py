#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], 'r')
        print("---", end="\n\n")
        for line in file:
            print(line, end="")
        print("\n\n---")
        file.close()
        if file.closed:
            print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
