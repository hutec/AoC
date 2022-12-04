use std::fs;

pub enum Outcome {
    Win,
    Loss,
    Draw,
}

#[derive(PartialEq, Clone)]
pub enum Shape {
    Rock,
    Paper,
    Scissors,
}

pub fn score_shape(shape: &Shape) -> i32 {
    match shape {
        Shape::Rock => 1,
        Shape::Paper => 2,
        Shape::Scissors => 3,
    }
}

pub fn score_outcome(outcome: &Outcome) -> i32 {
    match outcome {
        Outcome::Win => 6,
        Outcome::Draw => 3,
        Outcome::Loss => 0,
    }
}

fn duel(player1: &Shape, player2: &Shape) -> Outcome {
    // Returns the output for player 1
    match (player1, player2) {
        (Shape::Rock, Shape::Paper) => Outcome::Loss,
        (Shape::Rock, Shape::Scissors) => Outcome::Win,
        (Shape::Paper, Shape::Rock) => Outcome::Win,
        (Shape::Paper, Shape::Scissors) => Outcome::Loss,
        (Shape::Scissors, Shape::Rock) => Outcome::Loss,
        (Shape::Scissors, Shape::Paper) => Outcome::Win,
        (player1, player2) if player1 == player2 => Outcome::Draw,
        _ => panic!("Invalid move"),
    }
}

pub fn parse(symbol: &str) -> Shape {
    match symbol {
        "A" => Shape::Rock,
        "B" => Shape::Paper,
        "C" => Shape::Scissors,
        "X" => Shape::Rock,
        "Y" => Shape::Paper,
        "Z" => Shape::Scissors,
        _ => panic!("Invalid symbol"),
    }
}

pub fn main() {
    let lines: String = fs::read_to_string("../inputs/day02").expect("Can't read file");
    // Iterate over all lines and split into two values
    let mut total_score: i32 = 0;
    for line in lines.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let player1 = parse(parts[0]);
        let player2 = parse(parts[1]);
        total_score += score_outcome(&duel(&player2, &player1)) + score_shape(&player2);
    }

    // Print total score
    println!("Day 2 | Total score: {}", total_score);
}
