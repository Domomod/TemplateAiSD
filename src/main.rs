/* Run this simple example in Linux with following commands:
 * > cargo build
 * This will create a directory called "target", you can call the executable by writing:
 * > ./target/debug/hello_world
 * You can also use `cargo` to run the executable:
 * > cargo run
 *
 * In addition you are also provided with a launch.json task 'Debug Java hello_world' that launches a debug task in VS Code.
 *
 * Rust has a concept that (almost) everything is an expression. For example you can assign the result of an if-else statement 
 * or a block of code enclosed in curly braces {} to a variable, promoting concise and expressive coding patterns. Examples:
 * let var = if (a > b) {a} else {b};
 * let var = {let x=3; let y=5; x*y};
**/

mod hello_world;  // Import the `hello_world` module from the hello_worlds.rs file

// The main function, where the program execution begins.
fn main() {
    // Call the hello_world function and store the result in 'result'.
    // Syntax: let <variable_name> = <function_name>();
    let result = hello_world::hello_world();

    // Print the result to the console.
    println!("{}", result);
}