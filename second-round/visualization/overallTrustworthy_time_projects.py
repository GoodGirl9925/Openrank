import json
import matplotlib.pyplot as plt
import os

# 读取JSON数据
with open('../data/trustworthy_data/trustworthy_filtered.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 项目名称列表 project_names
project_names = ['PaddlePaddle', 'AdguardTeam', 'pingcap', 'cms-sw', 'microsoftgraph']

# 用于存储每个项目的时间和总可信值
project_data = {}

# 提取每个项目的总可信度值
for project_name in project_names:
    if project_name in data:
        project = data[project_name]
        dates = sorted(project['overall_trustworthy'].keys())  # 获取按时间排序的日期列表
        values = [project['overall_trustworthy'][date] for date in dates]  # 获取每个日期对应的可信值
        project_data[project_name] = (dates, values)

# 绘制折线图
plt.figure(figsize=(10, 6))

for project_name, (dates, values) in project_data.items():
    plt.plot(dates, values, label=project_name)

# 设置图表的标题和标签
plt.title('Overall Trustworthiness Over Time')
plt.xlabel('Time')
plt.ylabel('Overall Trustworthiness')
plt.xticks(rotation=45)
plt.grid(True)  # 启用网格
plt.legend(title='Projects')

# 显示图表
plt.tight_layout()  # 自动调整布局

# 保存图片
save_directory = "../data/visualization_result/"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

save_path = "../data/visualization_result/overallTrustworthy_time_projects_line_chart.png"
plt.savefig(save_path)

# plt.show()
