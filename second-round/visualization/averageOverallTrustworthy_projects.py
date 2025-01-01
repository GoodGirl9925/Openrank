import json
import matplotlib.pyplot as plt
import numpy as np
import os

# 从文件读取数据
file_path = "../data/trustworthy_data/trustworthy_filtered.json"
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 函数：计算每个项目的平均可信度
def calculate_average_trustworthy(project_data):
    overall_trustworthy = project_data.get('overall_trustworthy', {})
    values = list(overall_trustworthy.values())
    if values:
        return np.mean(values)  # 计算平均值
    return 0  # 如果没有可信值数据，返回0

# 存储每个项目的平均可信度
project_names = []
average_trustworthiness = []

# 遍历所有项目并计算平均可信值
for project_name, project_data in data.items():
    avg_trustworthy = calculate_average_trustworthy(project_data)
    project_names.append(project_name)
    average_trustworthiness.append(avg_trustworthy)

# 将项目名称和平均可信值打包为元组，并按可信值从大到小排序
sorted_projects = sorted(zip(average_trustworthiness, project_names), reverse=False, key=lambda x: x[0])

# 解压排序后的项目名称和可信值
sorted_average_trustworthiness, sorted_project_names = zip(*sorted_projects)

# 计算可信值的最大值和最小值
min_value = min(sorted_average_trustworthiness)
max_value = max(sorted_average_trustworthiness)

# 计算区间的边界值（分为5个区间）
interval = (max_value - min_value)
class_bound = [0.05, 0.15, 0.35, 0.6]
intervals = [min_value + i * interval for i in class_bound]  # 分别是第1, 2, 3, 4个区间的边界

# 为每个项目分配颜色
colors = []
for avg in sorted_average_trustworthiness:
    if avg <= intervals[0]:
        colors.append('#FFCC99')  # 第一分区（最小值到第1个区间边界）
    elif avg <= intervals[1]:
        colors.append('#A8D0E6')  # 第二分区（第1个区间边界到第2个区间边界）
    elif avg <= intervals[2]:
        colors.append('#BCE55C')  # 第三分区（第2个区间边界到第3个区间边界）
    elif avg <= intervals[3]:
        colors.append('#F79F81')  # 第四分区（第3个区间边界到第4个区间边界）
    else:
        colors.append('#C8BFE7')  # 第五分区（第4个区间边界到最大值）

# 使用Matplotlib绘制横向的条形图
plt.figure(figsize=(10, 16), dpi=200)  # 可以根据需要调整图表尺寸
bars = plt.barh(sorted_project_names, sorted_average_trustworthiness, color=colors)

# 设置标题和标签
plt.title("Average Trustworthiness of Projects", fontsize=16)
plt.xlabel("Average Trustworthiness", fontsize=12)
plt.ylabel("Project Name", fontsize=12)

# 为每个条形添加数值标签
for bar in bars:
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2,
             f'{bar.get_width():.2f}', va='center', ha='left', fontsize=10)

# 美化图表
plt.tight_layout()

# 保存图片
save_directory = "../data/visualization_result/"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

save_path = "../data/visualization_result/averageOverallTrustworthy_projects_bar_chart.png"
plt.savefig(save_path)

# 显示图表
# plt.show()
