package main

import (
    "flag"
    "fmt"
    "os"

    "github.com/mozillazg/go-unidecode"
)

func main() {
    inputFile := flag.String("i", "input.txt", "path to the input file (default: input.txt)")
    outputFile := flag.String("o", "output.txt", "path to the output file (default: output.txt)")
    flag.Parse()

    unicodeText, err := os.ReadFile(*inputFile)
    if err != nil {
        fmt.Printf("Error reading input file: %v\n", err)
        os.Exit(1)
    }

    asciiText := unidecode.Unidecode(string(unicodeText))

    err = os.WriteFile(*outputFile, []byte(asciiText), 0644)
    if err != nil {
        fmt.Printf("Error writing output file: %v\n", err)
        os.Exit(1)
    }

    fmt.Printf("Converted text written to %s\n", *outputFile)
}