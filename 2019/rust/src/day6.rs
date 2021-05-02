use regex::Regex;
use std::collections::HashMap;
use std::fs;

fn count_orbits(orbits: &HashMap<&str, &str>, orbiter: &str, acc: i32) -> i32 {
    match orbits.get(orbiter) {
        Some(center) => count_orbits(orbits, center, acc + 1),
        None => acc,
    }
}

pub fn main() {
    let input = fs::read_to_string("inputs/day6").expect("Can't read file");
    let lines = input.lines();
    let re = Regex::new(r"^([\d\w]*)\)([\d\w]*)$").unwrap();
    let mut orbits = HashMap::new();

    // Build orbit hashmap
    for line in lines {
        let caps = re.captures(line).unwrap();
        let center = caps.get(1).unwrap().as_str();
        let orbiter = caps.get(2).unwrap().as_str();
        orbits.insert(orbiter, center);
    }

    let count = orbits
        .keys()
        .map(|k| count_orbits(&orbits, k, 0))
        .sum::<i32>();
    println!("Result Task 1: {}", count);
}
