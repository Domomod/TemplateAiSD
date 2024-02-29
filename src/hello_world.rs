// Import necessary items from the chrono crate.
use chrono::{DateTime, Local};

// Define a function named hello_world.
// Syntax: <accessiblity> fn <function_name>() -> <return_type> {
pub fn hello_world() -> String {
    // Get the current date and time in the local time zone.
    // Syntax: let <variable_name> : <variable_type> = <expression>;
    let chrono_now: DateTime<Local> = Local::now();

    // Format the date as a string in the "YYYY-MM-DD" format.
    let time_stamp = chrono_now.format("%Y-%m-%d");

    // Build a greeting string including the formatted date.
    // Rust allows return statements to be implicit (ne need to write 'return')
    // https://stackoverflow.com/questions/27961879/why-is-using-return-as-the-last-statement-in-a-function-considered-bad-style
    format!("Hello, World! Today is {}!", time_stamp)
}
