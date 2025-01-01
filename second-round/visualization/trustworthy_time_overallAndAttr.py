import json
import matplotlib.pyplot as plt
import numpy as np
import os


def plot_trustworthy_data(project_name, file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    overall_trustworthy = data[project_name]["overall_trustworthy"]
    attribute_trustworthy = data[project_name]["attribute_trustworthy"]

    dates = list(overall_trustworthy.keys())
    overall_values = list(overall_trustworthy.values())

    availability = []
    reliability = []
    security = []
    timeliness = []
    maintainability = []
    survivability = []

    for date in dates:
        attrs = attribute_trustworthy[date]
        availability.append(attrs.get('availability', np.nan))
        reliability.append(attrs.get('reliability', np.nan))
        security.append(attrs.get('security', np.nan))
        timeliness.append(attrs.get('timeliness', np.nan))
        maintainability.append(attrs.get('maintainability', np.nan))
        survivability.append(attrs.get('survivability', np.nan))

    # 应用移动平均使曲线平滑
    window_size = 1 # 移动平均窗口大小，可以调整
    overall_values_smoothed = np.convolve(overall_values, np.ones(window_size) / window_size, mode='same')
    availability_smoothed = np.convolve(availability, np.ones(window_size) / window_size, mode='same')
    reliability_smoothed = np.convolve(reliability, np.ones(window_size) / window_size, mode='same')
    security_smoothed = np.convolve(security, np.ones(window_size) / window_size, mode='same')
    timeliness_smoothed = np.convolve(timeliness, np.ones(window_size) / window_size, mode='same')
    maintainability_smoothed = np.convolve(maintainability, np.ones(window_size) / window_size, mode='same')
    survivability_smoothed = np.convolve(survivability, np.ones(window_size) / window_size, mode='same')

    plt.figure(figsize=(10, 6))

    # 绘制总的可信值，加粗
    plt.plot(dates, overall_values_smoothed, label='Overall Trustworthy', linewidth=4)
    plt.plot(dates, availability_smoothed, label='Availability')
    # plt.plot(dates, reliability_smoothed, label='Reliability')
    # plt.plot(dates, security_smoothed, label='Security')
    plt.plot(dates, timeliness_smoothed, label='Timeliness')
    plt.plot(dates, maintainability_smoothed, label='Maintainability')
    plt.plot(dates, survivability_smoothed, label='Survivability')

    plt.xlabel('Date')
    plt.ylabel('Trustworthy Value')
    plt.title(f'Trustworthy Metrics for {project_name}')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # 保存图片
    save_directory = "../data/visualization_result/"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    save_path = "../data/visualization_result/trustworthy_time_overallAndAttr_line_chart.png"
    plt.savefig(save_path)

    # plt.show()


if __name__ == '__main__':
    project_name = "home-assistant"
    file_path = "../data/trustworthy_data/trustworthy_origin.json"
    plot_trustworthy_data(project_name, file_path)
