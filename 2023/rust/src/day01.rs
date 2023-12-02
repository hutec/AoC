use lazy_static::lazy_static;
use regex::Regex;
use std::fs;

lazy_static! {
    static ref FORWARD_RE: Regex =
        Regex::new(r"([1-9]|one|two|three|four|five|six|seven|eight|nine)").unwrap();
    static ref BACKWARD_RE: Regex =
        Regex::new(r"([1-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)").unwrap();
}

fn part2(line: &str) -> u32 {
    // Find the first number
    // Number is either 1-9, or one, two three, ..., nine

    // Find first occurence of forward regex
    let first = FORWARD_RE.find(line).unwrap();
    // Find last occurence of backward regex
    // Reverse line
    let reverse_line = line.chars().rev().collect::<String>();
    let last = BACKWARD_RE.find(&reverse_line).unwrap();

    // Map match to number
    let first_number = match first.as_str() {
        "one" => 1,
        "two" => 2,
        "three" => 3,
        "four" => 4,
        "five" => 5,
        "six" => 6,
        "seven" => 7,
        "eight" => 8,
        "nine" => 9,
        _ => first.as_str().parse::<u32>().unwrap(),
    };

    let last_number = match last.as_str() {
        "eno" => 1,
        "owt" => 2,
        "eerht" => 3,
        "ruof" => 4,
        "evif" => 5,
        "xis" => 6,
        "neves" => 7,
        "thgie" => 8,
        "enin" => 9,
        _ => last.as_str().parse::<u32>().unwrap(),
    };

    return first_number * 10 + last_number;
}

pub fn main() {
    // Part 1
    let numbers: Vec<u32> = fs::read_to_string("../inputs/01")
        .expect("Can't read file")
        .lines()
        .map(|line| line.chars().filter(|c| c.is_digit(10)).collect())
        .map(|digits: Vec<char>| {
            digits.first().unwrap().to_digit(10).unwrap() * 10
                + digits.last().unwrap().to_digit(10).unwrap()
        })
        .collect();

    let part1 = numbers.iter().sum::<u32>();
    println!("Day 01 - Part 1: {}", part1);

    // Part 2
    let numbers: Vec<u32> = fs::read_to_string("../inputs/01")
        .expect("Can't read file")
        .lines()
        .map(|line| part2(line))
        .collect();

    let num2 = numbers.iter().sum::<u32>();
    println!("Day 01 - Part 2: {}", num2);
}
