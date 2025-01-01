import json
import csv
import numpy as np

# 读取 JSON 数据
with open("../data/trustworthy_data/trustworthy_origin.json", "r") as f:
    data = json.load(f)

# 准备 CSV 文件的列名
csv_file = "../data/trustworthy_data/project_trustworthy.csv"
header = ["project_name", "overall_trustworthy"]

# 打开 CSV 文件进行写入
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

    # 遍历每个项目名称（project_name）
    for project_name, project_data in data.items():
        overall_trustworthy = project_data.get("overall_trustworthy", {})

        # 计算 overall_trustworthy 的日期对应的平均值
        overall_values = list(overall_trustworthy.values())

        # 如果有数据，计算均值
        if overall_values:
            avg_value = np.mean(overall_values)
        else:
            avg_value = None  # 如果没有值，设置为 None

        # 写入到 CSV 文件
        writer.writerow([project_name, avg_value])

print(f"CSV file has been saved to {csv_file}")
