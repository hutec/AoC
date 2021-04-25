use std::fs;

fn main() {
    let lines = fs::read_to_string("input").expect("Can't read file");
    let v: Vec<i32> = lines.split("\n").filter_map(|w| w.parse().ok()).collect();

    let result: i32 = v.iter().map(|x| (x / 3) - 2).sum();
    println!("Result Task 1: {}", result);
}
