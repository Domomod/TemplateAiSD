# Makefile for a C++ project
# ---------------------------------
# Make is a build automation tool that automatically builds executable programs and libraries from source code by reading files called Makefiles.
# A Makefile is a configuration file that specifies how and when to compile and link the source code files of a program.

# Compiler and compiler flags
CXX = g++
CXXFLAGS = -std=c++11 -Iinclude

# Set the build mode (debug or release)
MODE ?= debug

# Check if MODE is set to either debug or release
check_mode:
ifeq ($(filter $(MODE),debug release),)
	$(error MODE must be set to either debug or release)
else
# Null operation prevents message "Nothing to be done" when MODE is set proprerly
	@: 
endif

# Adjust compiler flags based on the build mode
ifeq ($(MODE),release)
    CXXFLAGS += -O2  # Optimization for release mode
else
    CXXFLAGS += -g -Wall  # Debug symbols and warnings for debug mode
endif

# Directories and paths
BUILD_DIR = target
SRC_DIR = src
TARGET_DIR = $(BUILD_DIR)/$(MODE)
OBJ_DIR = $(TARGET_DIR)/obj
TARGET = $(TARGET_DIR)/hello_world

# List all source files in the src directory
SRC_FILES = $(wildcard $(SRC_DIR)/*.cpp)

# Generate a list of object files in the obj directory
OBJ_FILES = $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRC_FILES))

# Default target builds the executable
build: check_mode $(TARGET)

# Rule to compile object files from source files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Rule to link object files into the final executable
$(TARGET): $(OBJ_FILES)
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) $^ -o $@

# Clean target removes all generated files
clean:
	rm -rf $(OBJ_DIR) $(BUILD_DIR)

# Compile and Run
run: $(TARGET)
	./$(TARGET)

# Remove generated files and rebuild the project
rebuild: clean build
