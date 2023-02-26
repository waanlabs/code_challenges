use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() -> std::io::Result<()> {

    let file = File::open("./puzzle-input.txt")?;
    let reader = BufReader::new(file);

    let mut calories_sum_list: Vec<i32> = Vec::new();
    let mut calories_sum: i32 = 0;

    for line in reader.lines() {
        let line = line?;

        if !line.is_empty() {
            calories_sum += line.parse::<i32>().unwrap();

        } else {
            calories_sum_list.push(calories_sum);
            calories_sum = 0;
        }
    }
    calories_sum_list.push(calories_sum);

    println!("{}", calories_sum_list.iter().max().unwrap()); // 1st answer

    let mut calories_sum_list_sorted = calories_sum_list.clone();
    calories_sum_list_sorted.sort_by(|a, b| b.cmp(a));
    let sum_top_three: i32 = calories_sum_list_sorted.iter().take(3).sum();
    println!("{}", sum_top_three); // 2nd answer

    Ok(())
}
