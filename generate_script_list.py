import os
import json

# Define the base folder (the one containing all your project subfolders)
base_folder = "Python"

# Dictionary to store scripts by category (subfolder)
script_dict = {}

# Walk through all subdirectories
for root, dirs, files in os.walk(base_folder):
    category = os.path.basename(root)  # Category name = subfolder name
    if category == base_folder:  
        continue  # Skip the root folder itself

    script_dict[category] = [
        os.path.join(category, file).replace("\\", "/") 
        for file in files if file.endswith(".py")
    ]

# Save the script list to a JSON file
with open(os.path.join(base_folder, "scripts.json"), "w") as f:
    json.dump(script_dict, f, indent=4)

print("✅ Script list updated! Check scripts.json")
