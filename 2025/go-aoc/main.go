package main

import (
	"aoc2025/day01"
	"flag"
	"fmt"
	"os"
	"time"
)

type Solution interface {
	Part1() (string, error)
	Part2() (string, error)
}

func main() {
	day := flag.Int("day", 1, "which day to run (1-25)")
	part := flag.Int("part", 0, "which part to run (0 for both, 1 or 2 for specific part)")
	flag.Parse()

	solutions := map[int]Solution{
		1: day01.New(),
		// Add more days as you complete them
	}

	solver, ok := solutions[*day]
	if !ok {
		fmt.Fprintf(os.Stderr, "Day %d not implemented yet\n", *day)
		os.Exit(1)
	}

	fmt.Printf("=== Advent of Code 2025 - Day %d ===\n\n", *day)

	if *part == 0 || *part == 1 {
		runPart(solver.Part1, 1)
	}

	if *part == 0 || *part == 2 {
		runPart(solver.Part2, 2)
	}
}

func runPart(fn func() (string, error), partNum int) {
	start := time.Now()
	result, err := fn()
	elapsed := time.Since(start)

	if err != nil {
		fmt.Printf("Part %d: ERROR - %v\n", partNum, err)
		return
	}

	fmt.Printf("Part %d: %s\n", partNum, result)
	fmt.Printf("Time: %v\n\n", elapsed)
}
