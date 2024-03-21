use std::io::{self, BufRead};
use std::io::{self, BufRead};
use std::fs::OpenOptions;
use std::io::Write;

fn main() {
    println!("Welcome to the News App!");

    loop {
        println!("Please enter a news headline (or 'exit' to quit):");

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");

        let input = input.trim();

        if input == "exit" {
            break;
        }

        println!("You entered: {}", input);

        // Open the file in append mode
     