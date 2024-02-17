use std::fs::File;
use std::io::prelude::*;

fn main() {
    let file_name = "rusty_files.txt";
    let mut file = File::create(file_name).expect("Failed to create file");

    // Write content to the file
    let content = "This is a new file created by Rust";
    file.write_all(content.as_bytes())
        .expect("Failed to write to file");

    println!("New file '{}' created successfully!", file_name);
}
