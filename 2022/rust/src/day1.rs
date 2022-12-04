use std::fs;

pub fn main() {
    let lines = fs::read_to_string("../inputs/day01").expect("Can't read file");

    let mut calories_per_elf = std::collections::HashMap::new();

    let mut counter = 0;
    for line in lines.lines() {
        if line.is_empty() {
            counter += 1;
        } else {
            let calories = line.parse::<i32>().expect("Can't parse line");
            *calories_per_elf.entry(counter).or_insert(0) += calories;
        }
    }
    let max_calories = calories_per_elf.iter().max_by_key(|entry| entry.1).unwrap();
    println!("Day 1 | Max calories: {:?}", max_calories);

    let mut calories: Vec<i32> = calories_per_elf.values().cloned().collect();
    calories.sort();
    let top_three = calories.iter().rev().take(3).sum::<i32>();
    println!("Day 1 | Top three: {}", top_three);
}
