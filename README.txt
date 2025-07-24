Rock Paper Scissors Game - Build Instructions

This project contains a simple Rock Paper Scissors game written in Python.

Build Automation Script:

- The script 'build.py' automates the build process by:
  1. Cleaning all __pycache__ directories to keep the workspace clean.
  2. Running unit tests to ensure the code works correctly.
  3. Creating a deployable zip package with all source Python files, excluding tests and cache.

To run the build script:

Make sure Python is installed on your system. Open your terminal or command prompt and run:

python build.py

If all unit tests pass, the script will generate a zip package named 'rps_game_package.zip' which you can use to deploy the application.