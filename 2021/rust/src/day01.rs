use std::fs;

pub fn main() {
    let numbers: Vec<i32> = fs::read_to_string("../inputs/1")
        .expect("Can't read file")
        .lines()
        .map(|line| line.parse::<i32>().unwrap())
        .collect();

    let part1 = numbers
        .windows(2)
        .map(|window| (window[0] < window[1]) as i32)
        .sum::<i32>();

    let part2 = numbers
        .windows(3)
        .map(|window| window.iter().sum::<i32>())
        .collect::<Vec<i32>>()
        .windows(2)
        .map(|window| (window[0] < window[1]) as i32)
        .sum::<i32>();

    println!("Day 1 - Part 1: {}", part1);
    println!("Day 1 - Part 2: {}", part2);
}
