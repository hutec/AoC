use std::fs;

// Import Outcome from day2_1.rs
use crate::day2_1::parse;
use crate::day2_1::score_outcome;
use crate::day2_1::score_shape;
use crate::day2_1::Outcome;
use crate::day2_1::Shape;

fn parse_outcome(symbol: &str) -> Outcome {
    match symbol {
        "X" => Outcome::Loss,
        "Y" => Outcome::Draw,
        "Z" => Outcome::Win,
        _ => panic!("Invalid symbol"),
    }
}

fn what_to_pick(outcome: &Outcome, shape: &Shape) -> Shape {
    // Returns the shape that would yield the given outcome against the given shape
    match (outcome, shape) {
        (Outcome::Win, Shape::Rock) => Shape::Paper,
        (Outcome::Win, Shape::Paper) => Shape::Scissors,
        (Outcome::Win, Shape::Scissors) => Shape::Rock,
        (Outcome::Loss, Shape::Rock) => Shape::Scissors,
        (Outcome::Loss, Shape::Paper) => Shape::Rock,
        (Outcome::Loss, Shape::Scissors) => Shape::Paper,
        (Outcome::Draw, shape) => shape.clone(),
    }
}

pub fn main() {
    let lines: String = fs::read_to_string("../inputs/day02").expect("Can't read file");
    // Iterate over all lines and split into two values
    let mut total_score: i32 = 0;
    for line in lines.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let player1 = parse(parts[0]);
        let target_outcome = parse_outcome(parts[1]);
        let shape = what_to_pick(&target_outcome, &player1);
        total_score += score_outcome(&target_outcome) + score_shape(&shape);
    }

    println!("Total score: {}", total_score);
}
