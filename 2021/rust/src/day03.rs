use std::fs;

fn count(lines: &Vec<&str>, idx: usize) -> (i32, i32) {
    let mut ones = 0;
    let mut zeros = 0;
    for line in lines {
        if line.chars().nth(idx).unwrap() == '1' {
            ones += 1;
        } else {
            zeros += 1;
        }
    }
    (ones, zeros)
}
pub fn main() {
    let file_content = fs::read_to_string("../inputs/3").expect("Can't read file");
    let lines: Vec<&str> = file_content.lines().collect();

    let mut gamma_rate: String = "".to_string(); // most common bits per column
    let mut epsilon_rate: String = "".to_string(); // least common bits per column
    for idx in 0..lines[0].len() {
        let (ones, zeros) = count(&lines, idx);
        gamma_rate += if ones > zeros { "1" } else { "0" };
        epsilon_rate += if ones < zeros { "1" } else { "0" };
    }

    let gamma_rate_int = u32::from_str_radix(&gamma_rate, 2).unwrap();
    let epsilon_rate_int = u32::from_str_radix(&epsilon_rate, 2).unwrap();
    println!("Day 3 - Part 1: {}", gamma_rate_int * epsilon_rate_int);
}
