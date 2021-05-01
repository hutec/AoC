use std::fs;

fn compute_fuel(mass: i32) -> i32 {
    (mass / 3) - 2
}

fn compute_fuel_recursive(mass: i32, acc: i32) -> i32 {
    let fuel = compute_fuel(mass);
    if fuel <= 0 {
        acc
    } else {
        compute_fuel_recursive(fuel, acc + fuel)
    }
}

pub fn main() {
    let lines = fs::read_to_string("inputs/day1").expect("Can't read file");
    let v: Vec<i32> = lines.split("\n").filter_map(|w| w.parse().ok()).collect();

    let result_1: i32 = v.iter().map(|&x| compute_fuel(x)).sum();
    println!("Result Task 1: {}", result_1);

    let result_2: i32 = v.iter().map(|&x| compute_fuel_recursive(x, 0)).sum();
    println!("Result Task 2: {}", result_2);
}
