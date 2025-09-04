import json

def machines_to_json(txt_file, json_file, group_size=8):
    # Read machines list
    with open(txt_file, "r") as f:
        machines = [line.strip() for line in f if line.strip()]
    
    # Split into groups of group_size
    grouped = {}
    for i in range(0, len(machines), group_size):
        key = str(i // group_size + 1)  # "1", "2", "3", ...
        grouped[key] = machines[i:i + group_size]
    
    # Write to JSON
    with open(json_file, "w") as f:
        json.dump(grouped, f, indent=4)

# Example usage
machines_to_json("machines_clean", "machines2.json")

# def remove_duplicates(input_file, output_file):
#     seen = set()
#     unique_lines = []

#     with open(input_file, "r") as f:
#         for line in f:
#             line = line.strip()
#             if line and line not in seen:  # ignore empty + duplicates
#                 seen.add(line)
#                 unique_lines.append(line)

#     with open(output_file, "w") as f:
#         for line in unique_lines:
#             f.write(line + "\n")

# # Example usage
# remove_duplicates("435_machines", "machines_clean")

