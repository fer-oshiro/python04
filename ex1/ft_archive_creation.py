#!/usr/bin/env python3
import sys


def get_content(filename: str) -> list[str]:
    print(f"Accessing file '{filename}'")
    try:
        file = open(filename, 'r')
        print("---", end="\n\n")
        data = file.read()
        print(data)
        print("\n---")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error opening file '{filename}': {e}")
        return []
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")
    return data.splitlines(keepends=True)


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
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    for line in content:
        file.write(line)
    file.close()
    print(f"Data saved in file '{file_name}'.")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = get_content(sys.argv[1])
    if not content:
        return
    print("\nTransform data:")
    content = transform_data(content)
    file_name = input("Enter new file name (or empty): ")
    if not file_name:
        return print("Not saving data.")
    write_content(file_name, content)


if __name__ == "__main__":
    main()
