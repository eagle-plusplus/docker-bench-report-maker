import re
import json
import os

# Define the tags to search for
tags = ["[WARN]", "[NOTE]", "[INFO]", "[PASS]"]

# Define the titles to search for in descriptions
titles = [
    "Host Configuration",
    "Docker daemon configuration",
    "Docker daemon configuration files",
    "Container Images and Build File",
    "Container Runtime",
    "Docker Security Operations",
    "Checks:",
    "Score:"
]

# Define a function to remove ANSI escape codes
def remove_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

# Define a function to check if any title is in the description
def contains_title(description):
    return any(title in description for title in titles)

# Define a function to extract tags and descriptions based on the tags
def extract_tags_and_descriptions(input_file):
    results = []
    
    try:
        with open(input_file, 'r') as file:
            for line in file:
                clean_line = remove_ansi_escape_codes(line).strip()
                for tag in tags:
                    if tag in clean_line:
                        # Extract the description part after the tag
                        description = clean_line.split(tag, 1)[-1].strip()
                        results.append({
                            'tag': tag,
                            'description': description,
                            'title': contains_title(description)
                        })
                        break
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError:
        print(f"Error: An IOError occurred while reading the file {input_file}.")
    
    return results

# Define the path to your input file and output JSON folder
input_file = 'docker_bench_logs.txt'
output_folder = 'json_output'
output_file = os.path.join(output_folder, 'docker-bench.json')

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Extract tags and descriptions
results = extract_tags_and_descriptions(input_file)

# Write results to a JSON file
with open(output_file, 'w') as file:
    json.dump(results, file, indent=4)

print(f"Results have been written to {output_file}")
