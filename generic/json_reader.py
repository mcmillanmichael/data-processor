import json

def read_file(json_file):
    """reads the given json file"""

    with open(json_file, 'r') as file:
        data = json.load(file)
    
    return data