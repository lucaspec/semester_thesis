import json
import os

''' INFO: Script that merges/concatenates all json files to one big file '''

concatenated_dict = {}

# Directory containing the JSON files
json_directory = "json"

# Output file path
output_file_path = "json_merged.json"

# Loop over all files in the directory with a .json extension
for filename in os.listdir(json_directory):
    if filename.endswith(".json"):
        with open(os.path.join(json_directory, filename)) as json_file:
            data = json.load(json_file)
            concatenated_dict.update(data)

# Save the concatenated dictionary to a new JSON file
with open(output_file_path, "w") as output_file:
    json.dump(concatenated_dict, output_file)
