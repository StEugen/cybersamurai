package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	//"os"
	"regexp"
	"strings"
)

type Payload struct {
	Chapters []string `json:"chapters"`
}

func main() {
	payloadFile := "toslice.json"
	payloadData, err := ioutil.ReadFile(payloadFile)
	if err != nil {
		log.Fatalf("Error reading payload file: %v", err)
	}

	var payload Payload
	if err := json.Unmarshal(payloadData, &payload); err != nil {
		log.Fatalf("Error parsing payload JSON: %v", err)
	}


	htmlFile := "input.html"
	htmlData, err := ioutil.ReadFile(htmlFile)
	if err != nil {
		log.Fatalf("Error reading HTML file: %v", err)
	}

	htmlString := string(htmlData)

	slicedHTML := make([]string, len(payload.Chapters))

	for i, chapter := range payload.Chapters {
		re := regexp.MustCompile(`(?i:<[^>]*>)*` + regexp.QuoteMeta(chapter) + `(?i:<[^>]*>)*`)
		match := re.FindStringIndex(htmlString)
		if match == nil {
			log.Printf("Chapter '%s' not found in HTML file", chapter)
			continue
		}

		startIndex := match[0]
		endIndex := strings.Index(htmlString[startIndex:], "<")

		chapterContent := htmlString[startIndex : startIndex+endIndex]

		chapterContent = cleanHTML(chapterContent)

		slicedHTML[i] = chapterContent
	}

	for i, chapterHTML := range slicedHTML {
		if chapterHTML != "" {
			outputFile := fmt.Sprintf("output_chapter_%d.html", i+1)
			if err := ioutil.WriteFile(outputFile, []byte(chapterHTML), 0644); err != nil {
				log.Printf("Error writing output file for chapter %d: %v", i+1, err)
				continue
			}
			fmt.Printf("Chapter %d sliced and saved to %s\n", i+1, outputFile)
		}
	}
}

func cleanHTML(html string) string {
	html = regexp.MustCompile(`<!--[\s\S]*?-->`).ReplaceAllString(html, "")

	html = strings.TrimSpace(html)

	return html
}

