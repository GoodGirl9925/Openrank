from TrustworthyPredictor import XGBoostPredictor
import json
import numpy as np
import pandas as pd


def extract_trustworthy_data(project_name, file_path="../data/trustworthy_data/trustworthy_origin.json"):
    # Step 1: Load the JSON data
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Step 2: Check if the project_name exists in the data
    if project_name not in data:
        raise ValueError(f"Project {project_name} not found in the data.")

    # Step 3: Extract 'overall_trustworthy' and 'attribute_trustworthy' for the project
    overall_trustworthy = data[project_name]["overall_trustworthy"]
    attribute_trustworthy = data[project_name]["attribute_trustworthy"]

    # Step 4: Initialize an empty 7x27 matrix (list of lists)
    seq = [[None] * len(overall_trustworthy) for _ in range(7)]

    # Fill the seq matrix
    dates = list(overall_trustworthy.keys())  # Get all the dates

    # 1. Extract 'overall_trustworthy' values (row 0 in seq)
    for i, date in enumerate(dates):
        seq[0][i] = overall_trustworthy[date]

    # 2. Extract values for 'availability', 'reliability', 'security', 'timeliness', 'maintainability', 'survivability'
    attributes = ["availability", "reliability", "security", "timeliness", "maintainability", "survivability"]
    for row_idx, attr in enumerate(attributes, start=1):
        for i, date in enumerate(dates):
            seq[row_idx][i] = attribute_trustworthy[date].get(attr, None)

    return seq



project_name = "home-assistant"
seq = extract_trustworthy_data(project_name)
# print(len(seq))
# print(len(seq[0]))
# print(seq)

predictor = XGBoostPredictor()
predictor.set_origin_seq(seq)
predicted_seq = predictor.get_predicted_seq()

# print(len(predicted_seq))
# print(len(predicted_seq[0]))
# print(predicted_seq)


# 将列表转换为NumPy数组
seq_array = np.array(seq)
predicted_seq_array = np.array(predicted_seq[:, :6])

# 水平堆叠两个数组
full_seq_array = np.hstack((seq_array, predicted_seq_array))
full_seq = full_seq_array.tolist()

# 取full_seq的第一行，即可信属性值
overall_trustworthy_full_seq = full_seq[0]

overall_trustworthy_rateOfChange_full_seq = []
if len(overall_trustworthy_full_seq) > 0:
    overall_trustworthy_rateOfChange_full_seq.append(0)
    for i in range(1, len(overall_trustworthy_full_seq)):
        prev = overall_trustworthy_full_seq[i - 1]
        current = overall_trustworthy_full_seq[i]
        rate_of_change = (current - prev) / prev
        overall_trustworthy_rateOfChange_full_seq.append(rate_of_change)

# print(overall_trustworthy_rateOfChange_full_seq)


# 定义日期范围
dates = [f"{year}-{month:02d}" for year in range(2021, 2024) for month in range(1, 13) if (
        year == 2021 or year == 2022 or (year == 2023 and month <= 9))]


# 保存为csv文件
df = pd.DataFrame({
    "时间": dates,
    "可信值": overall_trustworthy_full_seq,
    "变化率": overall_trustworthy_rateOfChange_full_seq
})
df.to_csv("../data/trustworthy_data/trustworthy_and_changeOfRate.csv", index=False)
