#include <iostream>
#include <string>
#include <chrono>
#include <sstream>
#include <iomanip>

std::string hello_world() {
    // Get the current time
    auto now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());

    // Build the formatted string using a stringstream
    std::stringstream resultStream;
    resultStream << "Hello, World! " << std::put_time(std::localtime(&now), "%Y-%m-%d") << "!";

    // Return the formatted string
    return resultStream.str();
}