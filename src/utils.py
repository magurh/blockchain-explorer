import json

def save_block(block_data, filename):
    """
    Saves block data to a JSON file.
    :param block_data: The block data dictionary.
    :param filename: The filename to save the JSON data.
    """
    with open(filename, "w") as json_file:
        json.dump(block_data, json_file, indent=4)
        print(f"Block data saved to {filename}")
