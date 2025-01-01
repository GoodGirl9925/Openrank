# 删除在计算过程中存在溢出的项目

import json


def remove_keys(keys_to_delete):
    input_data_path = "../data/trustworthy_data/trustworthy_origin.json"
    try:
        with open(input_data_path, 'r') as f:
            data = json.load(f)
        for key in keys_to_delete:
            data.pop(key, None)

        output_data_path = "../data/trustworthy_data/trustworthy_filtered.json"
        with open(output_data_path, 'w') as f:
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        print(f"The file {input_data_path} was not found.")
    except json.JSONDecodeError:
        print(f"There was an issue decoding the JSON file {input_data_path}.")


if __name__ == "__main__":
    keys_to_delete = ["airbytehq", "Azure", "project-chip"]
    remove_keys(keys_to_delete)
