# Makefile for Java

# Variables
JAVAC = javac
JAVA = java
JAVAP = javap

# Source and build directories
SRC_DIR = src
BUILD_DIR = target

# Main class
MAIN_CLASS = HelloWorld

# Source files
SRC_FILES = $(wildcard $(SRC_DIR)/*.java)

# Build target
TARGET = $(BUILD_DIR)/$(MAIN_CLASS).class

# Default target: build and run the program
build: $(TARGET)
	$(JAVA) -cp $(BUILD_DIR) $(MAIN_CLASS)

# Build target: compile the source files
$(TARGET): $(SRC_FILES)
	@mkdir -p $(BUILD_DIR)
	$(JAVAC) -d $(BUILD_DIR) $^

# Clean target: remove the build directory
clean:
	rm -rf $(BUILD_DIR)

# Run target: run the program
run: $(TARGET)
	$(JAVA) -cp $(BUILD_DIR) $(MAIN_CLASS)

# Display bytecode target: use javap to show bytecode
bytecode: $(TARGET)
	@$(foreach file, $(wildcard $(BUILD_DIR)/*.class), $(JAVAP) -c $(file);)

# Phony targets to avoid conflicts with file names
.PHONY: build clean run bytecode
