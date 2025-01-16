# File Renamer Script

This script is designed to rename all files in a specified directory by assigning them unique six-digit random numbers. This ensures that no two files have the same name and helps in organizing files with randomized identifiers.

## Features
- **Random Unique Naming**: Each file is assigned a unique six-digit random number to prevent name collisions.
- **Preservation of File Extensions**: The original file extensions are retained to ensure files remain accessible with their appropriate applications.
- **Automated Process**: Once the directory is set, the script handles the renaming process automatically.

## Usage
1. **Set the Directory**: Update the `directory` variable with the path to the directory containing the files you want to rename.
2. **Run the Script**: Execute the script in a Python environment.
3. **View Results**: After execution, all files in the specified directory will be renamed with unique six-digit numbers, and a success message will be displayed.

## Example
If the directory contains the following files:
```
example1.txt
example2.jpg
example3.pdf
```
After running the script, the files might be renamed as:
```
123456.txt
789012.jpg
345678.pdf
```

## Notes
- Ensure that the directory path is correctly specified.
- The script uses the `os` and `random` modules, which are included in the Python standard library.

## Disclaimer
- **Backup Recommended**: It's recommended to back up the original files before running the script, as the renaming process cannot be easily reversed.
- **Path Confidentiality**: The original path of the directory is hidden in this README to maintain confidentiality.
