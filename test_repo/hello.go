package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

// changelogEntry represents a single entry in the changelog.
type changelogEntry struct {
	Title     string
	Date      string
	Status    string
	PRNumber  string
	Bot       string
	Description string
}

// updateChangelog updates the CHANGELOG.md file with new entries.  Error handling is crucial for production use.
func updateChangelog(entries []changelogEntry) error {
	changelogFile, err := os.ReadFile("CHANGELOG.md")
	if err != nil {
		if os.IsNotExist(err) {
			changelogFile = []byte("# CHANGELOG\n\n") // Create file if it doesn't exist
		} else {
			return fmt.Errorf("failed to read CHANGELOG.md: %w", err)
		}
	}

	newEntries := ""
	for _, entry := range entries {
		newEntries += fmt.Sprintf("- %s (%s, %s, PR #%s by %s)\n    %s\n\n", entry.Date, entry.Status, entry.Title, entry.PRNumber, entry.Bot, entry.Description)
	}

	updatedChangelog := append(changelogFile, []byte(newEntries)...)
	return os.WriteFile("CHANGELOG.md", updatedChangelog, 0644)
}

func main() {
	// Example usage:  Replace with actual data retrieval from your bot/API.
	changelogEntries := []changelogEntry{
		{
			Date:      time.Now().Format("2006-01-02"),
			Status:    "Merged",
			Title:     "Fix: Resolved a critical bug in the authentication system",
			PRNumber:  "123",
			Bot:       "JuniorSoftwareAgent",
			Description: "This PR addresses a critical vulnerability in the authentication system, preventing unauthorized access.  The vulnerability was discovered during routine security testing.",
		},
		{
			Date:      time.Now().AddDate(0,0,-1).Format("2006-01-02"), // Yesterday's date
			Status:    "Closed",
			Title:     "Enhancement: Improved user experience on mobile devices",
			PRNumber:  "124",
			Bot:       "JuniorSoftwareAgent",
			Description: "This PR introduces several improvements to enhance the user experience on mobile devices.  Specifically, it addresses layout issues and improves responsiveness.",

		},
	}

	err := updateChangelog(changelogEntries)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error updating changelog: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("Changelog updated successfully!")
}
