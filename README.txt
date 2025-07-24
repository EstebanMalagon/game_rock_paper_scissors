# Rock Paper Scissors Game - Build Instructions

This project contains a simple Rock Paper Scissors game implemented in Python. 

## Build Automation Script

The `build.py` script helps automate the build process by doing the following:

1. Cleaning all `__pycache__` folders to keep the workspace clean.
2. Running unit tests to verify that the application works correctly.
3. Creating a deployable ZIP package containing all Python source files (excluding tests and cache).

## How to Run the Build Script

Make sure you have Python installed. Then run the following command in your project root directory:

```bash
python build.py
