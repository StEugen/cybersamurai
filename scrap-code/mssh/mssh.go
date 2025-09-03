// mssh.go
// Simple TUI SSH Manager in Go
// Requires: github.com/rivo/tview
// Install: go get github.com/rivo/tview

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strconv"

	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

type Host struct {
	Name         string `json:"name"`
	User         string `json:"user"`
	Host         string `json:"host"`
	Port         int    `json:"port"`
	IdentityFile string `json:"identity_file"`
	Notes        string `json:"notes"`
}

type AppState struct {
	Hosts     []Host
	StorePath string
}

func main() {
	app := tview.NewApplication()

	state := AppState{}
	state.StorePath = hostsFilePath()
	if err := os.MkdirAll(filepath.Dir(state.StorePath), 0o700); err != nil {
		log.Fatalf("failed to create config dir: %v", err)
	}

	if err := loadHosts(&state); err != nil {
		log.Printf("could not load hosts: %v", err)
	}

	table := tview.NewTable().SetBorders(false)
	help := tview.NewTextView().SetDynamicColors(true)
	help.SetText("[::b]Enter[::-] connect  [::b]a[::-] add  [::b]e[::-] edit  [::b]d[::-] delete  [::b]q[::-] quit")

	var layout *tview.Flex

	refreshTable := func() {
		table.Clear()
		table.SetCell(0, 0, tview.NewTableCell("Name").SetSelectable(false).SetAttributes(tcell.AttrBold))
		table.SetCell(0, 1, tview.NewTableCell("User@Host:Port").SetSelectable(false).SetAttributes(tcell.AttrBold))
		for i, h := range state.Hosts {
			r := i + 1
			left := tview.NewTableCell(h.Name)
			right := tview.NewTableCell(fmt.Sprintf("%s@%s:%d", h.User, h.Host, h.Port))
			left.SetReference(i)
			right.SetReference(i)
			table.SetCell(r, 0, left)
			table.SetCell(r, 1, right)
		}
	}

	refreshTable()

	makeForm := func(h *Host, onSave func(Host)) *tview.Form {
		f := tview.NewForm()
		name := ""
		user := ""
		host := ""
		port := "22"
		ident := ""
		notes := ""
		if h != nil {
			name = h.Name
			user = h.User
			host = h.Host
			port = strconv.Itoa(h.Port)
			ident = h.IdentityFile
			notes = h.Notes
		}
		f.AddInputField("Name", name, 40, nil, func(t string) { name = t })
		f.AddInputField("User", user, 40, nil, func(t string) { user = t })
		f.AddInputField("Host", host, 128, nil, func(t string) { host = t })
		f.AddInputField("Port", port, 6, func(textToCheck string, lastChar rune) bool {
			if lastChar < '0' || lastChar > '9' {
				return false
			}
			return true
		}, func(t string) { port = t })
		f.AddInputField("IdentityFile (optional)", ident, 200, nil, func(t string) { ident = t })
		f.AddInputField("Notes", notes, 200, nil, func(t string) { notes = t })
		f.AddButton("Save", func() {
			p, _ := strconv.Atoi(port)
			nh := Host{Name: name, User: user, Host: host, Port: p, IdentityFile: ident, Notes: notes}
			onSave(nh)
		})
		f.AddButton("Cancel", func() { app.SetRoot(layout, true).SetFocus(table) })
		f.SetBorder(true).SetTitle("Host")
		return f
	}

	layout = tview.NewFlex().SetDirection(tview.FlexRow)
	layout.AddItem(table, 0, 1, true)
	layout.AddItem(help, 1, 0, false)

	table.SetSelectable(true, false)
	table.SetSelectedFunc(func(row, col int) {
		if row == 0 {
			return
		}
		idx := row - 1
		connectHost(&state, idx, app)
	})

	app.SetInputCapture(func(event *tcell.EventKey) *tcell.EventKey {
		switch event.Rune() {
		case 'q':
			app.Stop()
		case 'a':
			form := makeForm(nil, func(nh Host) {
				state.Hosts = append(state.Hosts, nh)
				if err := saveHosts(&state); err != nil {
					log.Printf("save error: %v", err)
				}
				refreshTable()
				app.SetRoot(layout, true).SetFocus(table)
			})
			app.SetRoot(form, true).SetFocus(form)
		case 'e':
			row, _ := table.GetSelection()
			if row <= 0 {
				break
			}
			idx := row - 1
			h := state.Hosts[idx]
			form := makeForm(&h, func(nh Host) {
				state.Hosts[idx] = nh
				if err := saveHosts(&state); err != nil {
					log.Printf("save error: %v", err)
				}
				refreshTable()
				app.SetRoot(layout, true).SetFocus(table)
			})
			app.SetRoot(form, true).SetFocus(form)
		case 'd':
			row, _ := table.GetSelection()
			if row <= 0 {
				break
			}
			idx := row - 1

			modal := tview.NewModal().SetText(fmt.Sprintf("Delete %s?", state.Hosts[idx].Name)).AddButtons([]string{"Delete", "Cancel"}).SetDoneFunc(func(buttonIndex int, buttonLabel string) {
				if buttonLabel == "Delete" {
					state.Hosts = append(state.Hosts[:idx], state.Hosts[idx+1:]...)
					if err := saveHosts(&state); err != nil {
						log.Printf("save error: %v", err)
					}
					refreshTable()
				}
				app.SetRoot(layout, true).SetFocus(table)
			})
			app.SetRoot(modal, true).SetFocus(modal)
		}
		return event
	})

	if err := app.SetRoot(layout, true).EnableMouse(true).Run(); err != nil {
		log.Fatalf("error running app: %v", err)
	}
}

func hostsFilePath() string {
	cfg := os.Getenv("XDG_CONFIG_HOME")
	if cfg == "" {
		home, _ := os.UserHomeDir()
		cfg = filepath.Join(home, ".config")
	}
	return filepath.Join(cfg, "tuissh", "hosts.json")
}

func loadHosts(s *AppState) error {
	b, err := ioutil.ReadFile(s.StorePath)
	if err != nil {
		return err
	}
	if len(b) == 0 {
		s.Hosts = []Host{}
		return nil
	}
	return json.Unmarshal(b, &s.Hosts)
}

func saveHosts(s *AppState) error {
	b, err := json.MarshalIndent(s.Hosts, "", "  ")
	if err != nil {
		return err
	}
	return ioutil.WriteFile(s.StorePath, b, 0o600)
}

func connectHost(s *AppState, idx int, app *tview.Application) {
	if idx < 0 || idx >= len(s.Hosts) {
		return
	}
	h := s.Hosts[idx]
	args := []string{fmt.Sprintf("%s@%s", h.User, h.Host)}
	if h.Port != 0 && h.Port != 22 {
		args = append([]string{"-p", strconv.Itoa(h.Port)}, args...)
	}
	if h.IdentityFile != "" {
		args = append([]string{"-i", h.IdentityFile}, args...)
	}
	sshBin := "ssh"
	if runtime.GOOS == "windows" {
		sshBin = "ssh.exe"
	}

	app.Suspend(func() {
		cmd := exec.Command(sshBin, args...)
		cmd.Stdin = os.Stdin
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmd.Env = os.Environ()
		if err := cmd.Run(); err != nil {
			fmt.Fprintf(os.Stderr, "ssh failed: %v\n", err)
		}
	})
}

