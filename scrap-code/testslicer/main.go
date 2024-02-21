package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"

	"github.com/unidoc/unioffice/document"
)

func main() {
	chaptersFile, err := os.Open("chapters.json")
	if err != nil {
		fmt.Println("Error opening chapters.json file:", err)
		return
	}
	defer chaptersFile.Close()

	var chaptersMap map[string]string
	if err := json.NewDecoder(chaptersFile).Decode(&chaptersMap); err != nil {
		fmt.Println("Error decoding chapters.json:", err)
		return
	}

	doc, err := document.Open("input.docx")
	if err != nil {
		fmt.Println("Error opening input DOCX file:", err)
		return
	}
	defer doc.Close()

	for chapterName, pageRange := range chaptersMap {
		pages := strings.Split(pageRange, "-")
		startPage := toInt(pages[0])
		endPage := toInt(pages[1])

		if startPage > len(doc.Paragraphs()) || endPage > len(doc.Paragraphs()) {
			fmt.Println("Invalid page range for chapter", chapterName)
			continue
		}

		chapterDoc := document.New()

		for i := startPage - 1; i < endPage; i++ {
			chapterDoc.AddParagraph(doc.Paragraphs()[i].Clone())
		}

		chapterFileName := fmt.Sprintf("%s.docx", chapterName)
		if err := chapterDoc.SaveToFile(chapterFileName); err != nil {
			fmt.Println("Error saving chapter:", err)
			return
		}
		fmt.Println("Chapter", chapterName, "saved to", chapterFileName)
	}
}

func toInt(s string) int {
	i := 0
	for _, r := range s {
		i = i*10 + int(r-'0')
	}
	return i
}

