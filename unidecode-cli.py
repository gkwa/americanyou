import argparse

import unidecode

parser = argparse.ArgumentParser(description="Convert Unicode text to ASCII")
parser.add_argument(
    "-i",
    "--input",
    type=str,
    default="input.txt",
    help="path to the input file (default: input.txt)",
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    default="output.txt",
    help="path to the output file (default: output.txt)",
)

args = parser.parse_args()

with open(args.input, "r", encoding="utf-8") as file:
    unicode_text = file.read().strip()

ascii_text = unidecode.unidecode(unicode_text)

with open(args.output, "w", encoding="utf-8") as file:
    file.write(ascii_text)

print(f"Converted text written to {args.output}")
