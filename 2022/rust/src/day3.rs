use std::collections::HashSet;
use std::fs;

fn priority(item: char) -> i32 {
    if item.is_uppercase() {
        item as i32 - 38
    } else {
        item as i32 - 96
    }
}

fn part1(lines: &Vec<&str>) {
    let mut priority_sum = 0;
    for line in lines.iter() {
        // Split line in two halves
        let (left, right) = line.split_at(line.len() / 2);

        let left_set: HashSet<char> = left.chars().collect();
        let right_set: HashSet<char> = right.chars().collect();

        let intersection: Vec<char> = left_set.intersection(&right_set).cloned().collect();
        let shared_item = intersection[0];
        priority_sum += priority(shared_item);
    }

    println!("Day 3 | Priority sum: {}", priority_sum);
}

fn part2(lines: &Vec<&str>) {
    let mut priority_sum = 0;
    for groups in lines.chunks(3) {
        let mut intersection: HashSet<char> = groups[0].chars().collect();
        for line in groups.iter().skip(1) {
            intersection = intersection
                .intersection(&line.chars().collect())
                .cloned()
                .collect();
        }
        let shared_item = intersection.iter().next().unwrap();
        priority_sum += priority(shared_item.clone());
    }

    println!("Day 3 | Priority sum: {}", priority_sum);
}

pub fn main() {
    let lines: String = fs::read_to_string("../inputs/day03").expect("Can't read file");
    let lines = lines.lines().collect();
    part1(&lines);
    part2(&lines);
}
