package main

import (
	"fmt"
	"log"

	"github.com/shirou/gopsutil/disk"
	tgbotapi "gopkg.in/telegram-bot-api.v4"
)

const (
	tgToken     = ""
	chatID      = int64()
	alertSpaceTaken = 85 // in percents
)

func main() {
	bot, err := tgbotapi.NewBotAPI(tgToken)
	if err != nil {
		log.Fatal(err)
	}

	usedSpace, err := getUsedSpace("/")
	if err != nil {
		log.Println("Error getting left disk space:", err)
	} else {
		log.Printf("Used space: %d%%", usedSpace)
		if usedSpace >= alertSpaceTaken {
			message := fmt.Sprintf("Low disk space! %d%% taken", usedSpace)
			sendTelegramMessage(bot, chatID, message)
		}
	}
}

func getUsedSpace(path string) (int, error) {
	usage, err := disk.Usage(path)
	if err != nil {
		return 0, err
	}
	return int(usage.UsedPercent), nil
}

func sendTelegramMessage(bot *tgbotapi.BotAPI, chatID int64, message string) {
	msg := tgbotapi.NewMessage(chatID, message)
	_, err := bot.Send(msg)
	if err != nil {
		log.Println("Error sending message:", err)
	}
}













