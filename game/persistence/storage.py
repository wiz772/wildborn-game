import json
import settings
import copy

data_structure = {
    "scores": []
}

def get_data_from_json():
    try:
        with open(settings.DATA_FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError as e:
        return copy.deepcopy(data_structure)
    
def get_new_data_to_write(old_data, new_entry):
    return old_data + new_entry

def get_score_data(data):
    return data["scores"]
    
def write_data(data):
    json_str = json.dumps(data, indent=4)
    with open(settings.DATA_FILE_PATH, "w") as file:
        file.write(json_str)

def get_best_score(scores):
    return max(scores, default=0)