from Trustworthy import Trustworthy
import pandas as pd
import os
import json


# ----------读取数据----------
# 定义需要保存的变量名
file_names = [
    'normalized_activity.csv', 'normalized_attention.csv', 'normalized_bus_factor.csv',
    'normalized_change_request_age.csv', 'normalized_change_request_resolution_duration.csv',
    'normalized_change_request_response_time.csv', 'normalized_change_requests_reviews.csv',
    'normalized_code_change_lines_add.csv', 'normalized_code_change_lines_remove.csv',
    'normalized_code_change_lines_sum.csv', 'normalized_inactive_contributors.csv',
    'normalized_issue_age.csv', 'normalized_issue_resolution_duration.csv',
    'normalized_issue_response_time.csv', 'normalized_issues_and_change_request_active.csv',
    'normalized_issues_closed.csv', 'normalized_issues_new.csv', 'normalized_new_contributors.csv',
    'normalized_openrank.csv', 'normalized_participants.csv', 'normalized_stars.csv',
    'normalized_technical_fork.csv'
]

# 保存每个CSV文件对应的数据的字典
data_dict = {}

# 项目/公司名列表
project_list = []

# 逐一读取文件并处理
for file_name in file_names:
    # 读取CSV文件
    file_path = f"../data/normalized_data/{file_name}"
    df = pd.read_csv(file_path)

    # 选取第一列，作为项目/公司名列表
    df_project = df.iloc[:, 0:1]
    project_list = df_project.T.values.tolist()
    project_list = project_list[0]

    # 去掉第一列，并转置
    df = df.iloc[:, 1:]
    data = df.T.values.tolist()

    # 根据文件名动态命名变量
    variable_name = file_name.replace('normalized_', '').replace('.csv', '')
    data_dict[variable_name] = data

# 将所有处理后的数据存入对应的变量中
activity = data_dict.get('activity', [])
attention = data_dict.get('attention', [])
bus_factor = data_dict.get('bus_factor', [])
change_request_age = data_dict.get('change_request_age', [])
change_request_resolution_duration = data_dict.get('change_request_resolution_duration', [])
change_request_response_time = data_dict.get('change_request_response_time', [])
change_requests_reviews = data_dict.get('change_requests_reviews', [])
code_change_lines_add = data_dict.get('code_change_lines_add', [])
code_change_lines_remove = data_dict.get('code_change_lines_remove', [])
code_change_lines_sum = data_dict.get('code_change_lines_sum', [])
inactive_contributors = data_dict.get('inactive_contributors', [])
issue_age = data_dict.get('issue_age', [])
issue_resolution_duration = data_dict.get('issue_resolution_duration', [])
issue_response_time = data_dict.get('issue_response_time', [])
issues_and_change_request_active = data_dict.get('issues_and_change_request_active', [])
issues_closed = data_dict.get('issues_closed', [])
issues_new = data_dict.get('issues_new', [])
new_contributors = data_dict.get('new_contributors', [])
openrank = data_dict.get('openrank', [])
participants = data_dict.get('participants', [])
stars = data_dict.get('stars', [])
technical_fork = data_dict.get('technical_fork', [])

# print(activity[14]) # 0 <= index <= 14


# ----------计算可信值----------
dates = [f"{year}-{month:02d}" for year in range(2021, 2024) for month in range(1, 13) if (
            year == 2021 or year == 2022 or (year == 2023 and month <= 3))]

trustworthy_data = {}
for project_name in project_list:
    trustworthy_data[project_name] = {}
    trustworthy_data[project_name]['overall_trustworthy'] = {}
    trustworthy_data[project_name]['attribute_trustworthy'] = {}
    trustworthy_data[project_name]['subAttribute_trustworthy'] = {}

trustworthy = Trustworthy()

# print(project_list)

for i in range(0, len(activity)):
    trustworthy.set_trustworthy_score(activity[i], attention[i], bus_factor[i], change_request_age[i],
                                      change_request_resolution_duration[i], change_request_response_time[i],
                                      change_requests_reviews[i], code_change_lines_add[i], code_change_lines_remove[i],
                                      code_change_lines_sum[i], inactive_contributors[i], issue_age[i],
                                      issue_resolution_duration[i], issue_response_time[i],
                                      issues_and_change_request_active[i], issues_closed[i], issues_new[i],
                                      new_contributors[i], openrank[i], participants[i], stars[i], technical_fork[i])

    trustworthy.calculate_subAttributes()
    trustworthy.calculate_attributes()
    trustworthy.calculate_overall_trustworthy()

    date = dates[i]

    for project_index, project_name in enumerate(project_list):
        trustworthy_data[project_name]['overall_trustworthy'][date] = trustworthy.get_overall_trustworthy(project_index)
        trustworthy_data[project_name]['attribute_trustworthy'][date] = trustworthy.get_attribute_trustworthy(project_index)
        trustworthy_data[project_name]['subAttribute_trustworthy'][date] = trustworthy.get_subAttribute_trustworthy(project_index)


# ----------保存数据----------
trustworthy_data_path = "../data/trustworthy_data"

# 创建项目文件夹（如有必要）
os.makedirs(trustworthy_data_path, exist_ok=True)

with open(f'{trustworthy_data_path}/trustworthy_origin.json', 'w') as f:
    json.dump(trustworthy_data, f)
