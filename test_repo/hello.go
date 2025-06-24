package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

// changelogEntry represents a single entry in the changelog.
type changelogEntry struct {
	Title       string
	Description string
	Date        string
	Status      string
}

// generateChangelogEntry creates a formatted changelog entry.
func generateChangelogEntry(title, description, status string) changelogEntry {
	return changelogEntry{
		Title:       title,
		Description: description,
		Date:        time.Now().Format("2006-01-02"),
		Status:      status,
	}
}

// updateChangelog appends new entries to the changelog file.  Handles potential errors gracefully.
func updateChangelog(entries []changelogEntry, changelogPath string) error {
	changelogFile, err := os.OpenFile(changelogPath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return fmt.Errorf("failed to open changelog file: %w", err)
	}
	defer changelogFile.Close()

	for _, entry := range entries {
		newEntry := fmt.Sprintf("- %s (%s, %s):\n  %s\n\n", entry.Title, entry.Date, entry.Status, entry.Description)
		if _, err := changelogFile.WriteString(newEntry); err != nil {
			return fmt.Errorf("failed to write to changelog file: %w", err)
		}

	}
	return nil
}


func main() {
	// Example usage:  Replace with actual PR data retrieval.
	prEntries := []changelogEntry{
		generateChangelogEntry("Add feature X", "This feature adds functionality X.", "Merged"),
		generateChangelogEntry("Fix bug Y", "This commit fixes bug Y.", "Merged"),
		generateChangelogEntry("Improve performance Z", "Performance improvements for Z.", "In Progress"),

	}

	err := updateChangelog(prEntries, "CHANGELOG.md")
	if err != nil {
		fmt.Printf("Error updating changelog: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("Changelog updated successfully!")
}
