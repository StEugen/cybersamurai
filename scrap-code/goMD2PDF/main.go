package main

import (
	"fmt"
	"io/ioutil"
	"os"

	"github.com/jaytaylor/html2text"
	"github.com/russross/blackfriday"
	"github.com/signintech/gopdf"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: go run main.go input.md output.pdf")
		os.Exit(1)
	}

	inputFile := os.Args[1]
	outputFile := os.Args[2]

	markdownData, err := ioutil.ReadFile(inputFile)
	if err != nil {
		fmt.Println("Error reading Markdown file:", err)
		os.Exit(1)
	}

	htmlData := blackfriday.MarkdownCommon(markdownData)

	plainText, err := html2text.FromString(string(htmlData), html2text.Options{PrettyTables: true})
	if err != nil {
		fmt.Println("Error converting HTML to plain text:", err)
		os.Exit(1)
	}

	pdf := gopdf.GoPdf{}
	pdf.Start(gopdf.Config{PageSize: *gopdf.PageSizeA4})
	pdf.AddPage()

	err = pdf.AddTTFFont("arial", "./Arial.ttf")
	if err != nil {
		fmt.Println("Error adding TTF font:", err)
		os.Exit(1)
	}

	pdf.SetFont("arial", "", 12)

	pdf.Cell(nil, plainText)

	err = pdf.WritePdf(outputFile)
	if err != nil {
		fmt.Println("Error writing PDF file:", err)
		os.Exit(1)
	}

	fmt.Printf("Conversion successful. PDF saved to %s\n", outputFile)
}




