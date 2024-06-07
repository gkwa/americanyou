import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Convert ASCII file to Unicode UTF-8")
    parser.add_argument("input_file", type=str, help="Path to the input ASCII file")
    return parser.parse_args()


def read_ascii_file(file_path):
    with open(file_path, "r") as ascii_file:
        return ascii_file.read()


def write_utf8_to_stdout(content):
    sys.stdout.buffer.write(content.encode("utf-8"))


def main():
    args = parse_args()
    content = read_ascii_file(args.input_file)
    write_utf8_to_stdout(content)


if __name__ == "__main__":
    main()
