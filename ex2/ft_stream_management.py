#!/usr/bin/env python3
import sys


def get_content(file_name: str) -> list[str]:
    content = []
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
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}\n")
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
    try:
        file = open(file_name, 'w')
        for line in content:
            file.write(line)
        file.close()
        if file.closed:
            print(f"Data saved in file '{file_name}'.")
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}\n")
        print("Data not saved.")
        sys.exit(0)


def read_input(label: str) -> str:
    print(label, end="", flush=True)
    return sys.stdin.readline().rstrip("\n")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = get_content(sys.argv[1])
    print("\nTransform data:")
    content = transform_data(content)
    file_name = read_input("Enter new file name (or empty): ")
    if not file_name:
        return print("Not saving data.")
    print(f"Saving data to '{file_name}'", flush=True)

    write_content(file_name, content)


if __name__ == "__main__":
    main()
