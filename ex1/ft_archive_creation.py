#!/usr/bin/env python3
import sys


def get_content(file_name: str) -> list[str]:
    content = []
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name, 'r')
        print("---", end="\n\n")
        for line in file:
            print(line, end="")
            content.append(line)
        print("\n\n---")
        file.close()
        if file.closed:
            print(f"File '{file_name}' closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")
        sys.exit(1)
    return content


def transform_data(content: list[str]) -> list[str]:
    def update_line(line: str) -> str:
        if line[-1:] == "\n":
            return f"{line[:-1]}#\n"
        return f"{line}#"

    transform_content = []
    print("---", end="\n\n")
    for line in content:
        new_line = update_line(line)
        print(new_line, end="")
        transform_content.append(new_line)
    print("\n\n---")
    return transform_content


def write_content(file_name: str, content: list[str]) -> None:
    print(f"Saving data to '{file_name}'")
    try:
        file = open(file_name, 'w')
        for line in content:
            file.write(line)
        file.close()
        if file.closed:
            print(f"Data saved in file '{file_name}'.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")
        sys.exit(1)


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = get_content(sys.argv[1])
    print("\nTransform data:")
    content = transform_data(content)
    file_name = input("Enter new file name (or empty): ")
    if not file_name:
        return print("Not saving data.")

    write_content(file_name, content)


if __name__ == "__main__":
    main()
