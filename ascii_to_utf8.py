import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert ASCII text to Unicode UTF-8 with bold and italic styling"
    )
    parser.add_argument("text", type=str, help="ASCII text to convert")
    parser.add_argument("output_file", type=str, help="Path to the output file")
    return parser.parse_args()


def style_text(text):
    styled_text = ""
    for char in text:
        if char.isalpha():
            styled_char = chr(ord(char) + 0x68)
            styled_text += chr(ord(styled_char) + 0x1D400)
        else:
            styled_text += char
    return styled_text


def write_utf8_to_file(content, file_path):
    with open(file_path, "w", encoding="utf-8") as utf8_file:
        utf8_file.write(content)


def main():
    args = parse_args()
    styled_text = style_text(args.text)
    write_utf8_to_file(styled_text, args.output_file)


if __name__ == "__main__":
    main()
