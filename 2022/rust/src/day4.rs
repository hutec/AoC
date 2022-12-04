use std::fs;

struct Range {
    min: i32,
    max: i32,
}

impl Range {
    fn contains(&self, other: &Range) -> bool {
        self.min <= other.min && self.max >= other.max
    }

    fn overlaps(&self, other: &Range) -> bool {
        self.min <= other.max && self.max >= other.min
    }
}

pub fn main() {
    let lines: String = fs::read_to_string("../inputs/day04").expect("Can't read file");
    let lines: Vec<&str> = lines.lines().collect();
    let (contain_count, overlap_count) = lines
        .iter()
        .map(|line| {
            let mut ranges: Vec<Range> = Vec::new();
            for range in line.split(",") {
                let mut range = range.split("-");
                let min = range.next().unwrap().parse::<i32>().unwrap();
                let max = range.next().unwrap().parse::<i32>().unwrap();
                let range = Range { min, max };
                ranges.push(range);
            }
            (
                ranges[0].contains(&ranges[1]) || ranges[1].contains(&ranges[0]),
                ranges[0].overlaps(&ranges[1]),
            )
        })
        .fold(
            (0, 0),
            |(contain_count, overlap_count), (contain, overlap)| {
                (
                    contain_count + contain as i32,
                    overlap_count + overlap as i32,
                )
            },
        );

    println!("Day 4 | Contain count: {}", contain_count);
    println!("Day 4 | Overlap count: {}", overlap_count);
}
