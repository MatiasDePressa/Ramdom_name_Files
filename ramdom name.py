import os
import random

# Directory containing the files
directory = 'Your path'

# Get a list of all files in the directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Keep track of used numbers to avoid duplicates
used_numbers = set()

for file in files:
    # Generate a unique 6-digit random number
    while True:
        new_name = f"{random.randint(100000, 999999)}"
        if new_name not in used_numbers:
            used_numbers.add(new_name)
            break

    # Extract the file extension
    file_extension = os.path.splitext(file)[1]  # This gets the .txt, .jpg, etc.
    old_path = os.path.join(directory, file)
    new_path = os.path.join(directory, f"{new_name}{file_extension}")
    
    # Rename the file
    os.rename(old_path, new_path)
    print(f"Renamed '{file}' to '{new_name}{file_extension}'")

print("✅ All files have been renamed successfully!")
