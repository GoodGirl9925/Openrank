# 把opendigger_data中的数据整理为csv文件
# 列为项目名，行为日期（2022-01至2023-03）
# 若有缺失数据，直接删除整个项目，即删除整行

import json
import csv
import os

def adjust_opendigger_data(item_name):
    # input_dir = "../data/opendigger_data/"
    input_dir = "../data/top_300_metrics/"
    output_dir = "../data/adjusted_data/"
    output_file_path = output_dir + "adjusted_" + item_name + ".csv"

    # 如果输出目录不存在，创建它
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 定义日期范围
    dates = [f"{year}-{month:02d}" for year in range(2022, 2024) for month in range(1, 13) if (
            year == 2022 or (year == 2023 and month <= 3))]

    # 用于记录成功处理、数据不全、文件未找到、JSON解码错误的数量
    success_count = 0
    incomplete_data_count = 0
    file_not_found_count = 0
    json_decode_error_count = 0

    # 写入csv文件
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 先写入日期作为第一行
        writer.writerow(["Company"] + dates)
        for company in os.listdir(input_dir):
            company_path = os.path.join(input_dir, company)
            if os.path.isdir(company_path):
                sub_folders = [f for f in os.listdir(company_path) if os.path.isdir(os.path.join(company_path, f))]
                if sub_folders:
                    target_folder = os.path.join(company_path, sub_folders[0])
                else:
                    target_folder = company_path
                json_file_path = os.path.join(target_folder, f"{item_name}.json")
                try:
                    # 读取json数据
                    with open(json_file_path, 'r') as f:
                        data = json.load(f)

                    target_data = []
                    date_data_complete = True
                    for date in dates:
                        # 有些数据含有“avg”，有些没有，所以分别处理
                        if "avg" in data:
                            value = data["avg"].get(date)
                        else:
                            value = data.get(date)

                        if value is None:
                            date_data_complete = False
                            break
                        target_data.append(value)

                    if date_data_complete:
                        # 将公司名称和对应完整数据一起写入CSV文件
                        writer.writerow([company] + target_data)
                        success_count += 1
                        # print(f"成功处理第 {success_count} 条数据，对应公司为 {company}")
                    else:
                        incomplete_data_count += 1
                        # print(f"WARNING: 处理第 {success_count + incomplete_data_count} 条数据失败（数据不全），对应公司为 {company}")
                except FileNotFoundError:
                    file_not_found_count += 1
                    # print(f"WARNING: 处理第 {success_count + incomplete_data_count + file_not_found_count} 条数据失败（文件未找到），对应公司为 {company}")
                except json.JSONDecodeError:
                    json_decode_error_count += 1
                    # print(f"WARNING: 处理第 {success_count + incomplete_data_count + file_not_found_count + json_decode_error_count} 条数据失败（JSON解码错误），对应公司为 {company}")

    print(f"成功处理的数据条数: {success_count}")
    print(f"数据不全的数据条数: {incomplete_data_count}")
    print(f"文件未找到的数据条数: {file_not_found_count}")
    print(f"JSON解码错误的数据条数: {json_decode_error_count}")

item_name_list = [
    "activity",
    # "active_dates_and_times",
    "attention",
    "bus_factor",
    # "bus_factor_detail",
    "change_request_age",
    "change_request_resolution_duration",
    "change_request_response_time",
    "change_requests_reviews",
    "code_change_lines_add",
    "code_change_lines_remove",
    "code_change_lines_sum",
    # "contributor_email_suffixes",
    "inactive_contributors",
    "issues_and_change_request_active",
    "issues_closed",
    "issues_new",
    "issue_age",
    "issue_resolution_duration",
    "issue_response_time",
    "new_contributors",
    # "new_contributors_detail",
    "openrank",
    "participants",
    "stars",
    "technical_fork"
]


if __name__ == "__main__":
    for item_name in item_name_list:
        adjust_opendigger_data(item_name)
        print(f"Item \"{item_name}\" is done.")
