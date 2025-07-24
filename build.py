import os
import shutil
import subprocess
import sys
from zipfile import ZipFile

def clean_pycache():
    print("Cleaning __pycache__ folders...")
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                dir_path = os.path.join(root, d)
                print(f"Removing {dir_path}")
                shutil.rmtree(dir_path)
    print("Cleaning done.\n")

def run_tests():
    print("Running unit tests...")
    # Run all tests in the 'tests' folder matching test_*.py
    result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"])
    if result.returncode == 0:
        print("All tests passed successfully.\n")
    else:
        print("Some tests failed. Please check the output above.\n")
        sys.exit(1)

def create_package():
    print("Creating deployable zip package...")
    zip_filename = "rps_game_package.zip"
    with ZipFile(zip_filename, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk('.'):
            # Skip __pycache__ and tests folders
            if "__pycache__" in foldername or "tests" in foldername:
                continue
            for filename in filenames:
                if filename.endswith('.py'):
                    filepath = os.path.join(foldername, filename)
                    # Archive with relative path
                    arcname = os.path.relpath(filepath, '.')
                    zipf.write(filepath, arcname)
    print(f"Package created: {zip_filename}\n")

def main():
    print("Starting build process for Rock Paper Scissors game...\n")
    clean_pycache()
    run_tests()
    create_package()
    print("Build process completed. Ready to deploy!")

if __name__ == "__main__":
    main()
