use std::collections::HashMap;
use std::fs;

pub fn main() {
    let content = fs::read_to_string("../inputs/02").expect("Unable to read file");
    let lines: Vec<&str> = content.lines().collect();

    // Part 1
    let mut games: HashMap<i32, HashMap<String, i32>> = HashMap::new();
    for line in lines {
        let parts: Vec<&str> = line.split(":").collect();
        let game = parts[0];
        let draws = parts[1].trim();
        let id: i32 = game.split_whitespace().last().unwrap().parse().unwrap();

        let mut cubes: HashMap<String, i32> = HashMap::new();
        let re = regex::Regex::new(r"(\d+) (\w+)").unwrap();
        for caps in re.captures_iter(draws) {
            let count: i32 = caps[1].parse().unwrap();
            let color: String = caps[2].to_string();
            let entry = cubes.entry(color).or_insert(0);
            *entry = (*entry).max(count);
        }

        games.insert(id, cubes);
    }

    fn is_possible(cubes: &HashMap<String, i32>) -> bool {
        cubes.get("red").unwrap_or(&0) <= &12
            && cubes.get("green").unwrap_or(&0) <= &13
            && cubes.get("blue").unwrap_or(&0) <= &14
    }

    let sum_possible_games: i32 = games
        .iter()
        .filter(|(_, cubes)| is_possible(cubes))
        .map(|(&id, _)| id)
        .sum();
    println!("Day 02 - Part 1: {}", sum_possible_games);

    // Part 2
    let sum_powers: i32 = games
        .values()
        .map(|cubes| cubes.values().product::<i32>())
        .sum();
    println!("Day 02 - Part 2: {}", sum_powers);
}
