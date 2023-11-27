use std::fs;
use std::str::FromStr;
struct Position {
    x: i32,
    y: i32,
}

struct PositionAim {
    pos: Position,
    aim: i32,
}

#[derive(Copy, Clone)]
enum Direction {
    FORWARD,
    DOWN,
    UP,
}

impl FromStr for Direction {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "down" => Ok(Direction::DOWN),
            "up" => Ok(Direction::UP),
            "forward" => Ok(Direction::FORWARD),
            _ => Err(()),
        }
    }
}

fn move_ship_part1(dir: Direction, steps: i32, pos: Position) -> Position {
    match dir {
        Direction::FORWARD => Position {
            x: pos.x + steps,
            y: pos.y,
        },
        Direction::DOWN => Position {
            x: pos.x,
            y: pos.y + steps,
        },
        Direction::UP => Position {
            x: pos.x,
            y: pos.y - steps,
        },
    }
}

fn move_ship_part2(dir: Direction, steps: i32, pos: PositionAim) -> PositionAim {
    match dir {
        Direction::DOWN => PositionAim {
            pos: pos.pos,
            aim: pos.aim + steps,
        },
        Direction::UP => PositionAim {
            pos: pos.pos,
            aim: pos.aim - steps,
        },
        Direction::FORWARD => PositionAim {
            pos: Position {
                x: pos.pos.x + steps,
                y: pos.pos.y + pos.aim * steps,
            },
            aim: pos.aim,
        },
    }
}
pub fn main() {
    let course: Vec<(Direction, i32)> = fs::read_to_string("../inputs/2")
        .expect("Can't read file")
        .lines()
        .map(|line| {
            let mut split = line.split_whitespace();
            let dir = split.next().unwrap().parse::<Direction>().unwrap();
            let steps = split.next().unwrap().parse::<i32>().unwrap();
            (dir, steps)
        })
        .collect();

    let mut pos = Position { x: 0, y: 0 };
    for &(dir, steps) in &course {
        pos = move_ship_part1(dir, steps, pos);
    }
    println!("Day 2 - Part 1: {}", pos.x * pos.y);

    let mut pos = PositionAim {
        pos: Position { x: 0, y: 0 },
        aim: 0,
    };
    for &(dir, steps) in &course {
        pos = move_ship_part2(dir, steps, pos);
    }
    println!("Day 2 - Part 2: {}", pos.pos.x * pos.pos.y);
}
