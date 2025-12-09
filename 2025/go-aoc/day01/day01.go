package day01

import (
	"fmt"
	"strconv"

	"aoc2025/utils"
)

type Day01 struct {
	lines []string
}

func New() *Day01 {
	lines, err := utils.ReadLines("day01/input.txt")
	if err != nil {
		panic(err)
	}
	return &Day01{lines: lines}
}

func (d *Day01) Part1() (string, error) {
	position := 50
	password := 0
	for _, line := range d.lines {
		direction := line[0]
		distance, err := strconv.Atoi(line[1:])
		if err != nil {
			panic(err)
		}
		if direction == 'L' {
			position = (position - distance) % 100
		} else {
			position = (position + distance) % 100
		}
		if position == 0 {
			password += 1
		}
	}
	return fmt.Sprintf("%d", password), nil
}

func mod(a, b int) int {
	return (a%b + b) % b
}

func divmod(numerator, denominator int) (quotient, remainder int) {
	quotient = numerator / denominator // integer division, decimals are truncated
	remainder = numerator % denominator
	return
}

func (d *Day01) Part2() (string, error) {
	position := 50
	password := 0
	for _, line := range d.lines {
		direction := line[0]
		distance, err := strconv.Atoi(line[1:])
		if err != nil {
			panic(err)
		}

		passes, remainder := divmod(distance, 100)
		if direction == 'L' {
			if position != 0 && remainder > position {
				passes += 1
			}
			position = mod(position-remainder, 100)
		} else {
			if position != 0 && remainder > (100-position) {
				passes += 1
			}
			position = mod(position+remainder, 100)
		}
		if position == 0 {
			password += 1
		}
		password += passes

	}
	return fmt.Sprintf("%d", password), nil
}
