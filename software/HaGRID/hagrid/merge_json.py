import json
import os
import sys

''' INFO: Script that merges/concatenates all json files to one big file '''

# Check if the correct number of arguments is provided
if len(sys.argv) < 3:
    print("Usage: python script.py json_directory output_file_path")
    sys.exit(1)

# Retrieve arguments from command line
json_directory = str(sys.argv[1])
output_file_path = str(sys.argv[2])

# New dictionary containing merged json files
concatenated_dict = {}

# Loop over all files in the directory with a .json extension
for filename in os.listdir(json_directory):
    if filename.endswith(".json"):
        with open(os.path.join(json_directory, filename)) as json_file:
            data = json.load(json_file)
            concatenated_dict.update(data)

# Save the concatenated dictionary to a new JSON file
with open(output_file_path, "w") as output_file:
    json.dump(concatenated_dict, output_file)
