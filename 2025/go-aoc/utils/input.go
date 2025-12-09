package utils

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// ReadLines reads all lines from a file
func ReadLines(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return lines, nil
}

// ReadFile reads the entire file as a string
func ReadFile(filename string) (string, error) {
	content, err := os.ReadFile(filename)
	if err != nil {
		return "", err
	}
	return string(content), nil
}

// ReadInts reads lines and converts them to integers
func ReadInts(filename string) ([]int, error) {
	lines, err := ReadLines(filename)
	if err != nil {
		return nil, err
	}

	var nums []int
	for _, line := range lines {
		if line == "" {
			continue
		}
		num, err := strconv.Atoi(strings.TrimSpace(line))
		if err != nil {
			return nil, fmt.Errorf("failed to parse int from '%s': %w", line, err)
		}
		nums = append(nums, num)
	}

	return nums, nil
}

// SplitByBlankLines splits input into groups separated by blank lines
func SplitByBlankLines(content string) []string {
	return strings.Split(strings.TrimSpace(content), "\n\n")
}

// ParseIntList parses a comma or space separated list of integers
func ParseIntList(s string, separator string) ([]int, error) {
	parts := strings.Split(s, separator)
	nums := make([]int, 0, len(parts))

	for _, part := range parts {
		part = strings.TrimSpace(part)
		if part == "" {
			continue
		}
		num, err := strconv.Atoi(part)
		if err != nil {
			return nil, err
		}
		nums = append(nums, num)
	}

	return nums, nil
}

// MustReadLines reads lines or panics (useful for quick solutions)
func MustReadLines(filename string) []string {
	lines, err := ReadLines(filename)
	if err != nil {
		panic(err)
	}
	return lines
}

// MustReadFile reads file or panics
func MustReadFile(filename string) string {
	content, err := ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return content
}
