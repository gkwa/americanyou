import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Convert Unicode text to ASCII")
    parser.add_argument("text", type=str, help="Unicode text to convert")
    parser.add_argument("output_file", type=str, help="Path to the output file")
    return parser.parse_args()


def unicode_to_ascii(unicode_text):
    ascii_text = unicode_text.encode("ascii", errors="ignore").decode("ascii")
    return ascii_text


def write_ascii_to_file(content, file_path):
    with open(file_path, "w", encoding="ascii") as ascii_file:
        ascii_file.write(content)


def main():
    args = parse_args()
    ascii_text = unicode_to_ascii(args.text)
    write_ascii_to_file(ascii_text, args.output_file)


if __name__ == "__main__":
    main()
