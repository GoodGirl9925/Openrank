# 归一化每一个项目的所有指标数据

import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# filtered_code_change_lines_sum.csv所有元素取绝对值
def preprocess_filtered_code_change_lines_sum():
    # 读取 CSV 文件
    file_path = '../data/filtered_data/filtered_code_change_lines_sum.csv'
    df = pd.read_csv(file_path, index_col=0)

    # 对所有除了第一行和第一列之外的元素取绝对值
    df.iloc[:, :] = df.iloc[:, :].abs()

    # 将修改后的数据保存回原文件
    df.to_csv(file_path)

    print("文件filtered_code_change_lines_sum.csv已更新并保存。")


def normalize_filtered_data():
    # 设置文件目录路径
    input_dir = '../data/filtered_data'
    output_dir = '../data/normalized_data'

    # 如果输出目录不存在，创建它
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取所有csv文件
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    # 初始化线性归一化器，目标范围[1, 10]
    scaler = MinMaxScaler(feature_range=(1, 10))

    # 逐个处理csv文件
    for csv_file in csv_files:
        # 构建文件路径
        input_file = os.path.join(input_dir, csv_file)
        new_file_name = 'normalized' + csv_file[len('filtered'):]
        output_file = os.path.join(output_dir, new_file_name)

        # 读取csv文件
        df = pd.read_csv(input_file)

        # 保留第一列信息，并对后续列进行处理
        first_column = df.iloc[:, 0]  # 第一列
        df = df.iloc[1:, 1:]  # 取数据的其余部分

        # 对每个数值取对数
        # df = np.log(df + 1e-6)  # 加上1e-6以避免取对数时出现错误

        # df = np.exp(df)

        prev_df = df

        df = scaler.fit_transform(df)

        df = np.log(df)

        # 对每一列应用归一化操作
        normalized_df = pd.DataFrame(scaler.fit_transform(df), columns=prev_df.columns)

        # 将第一列添加回归一化后的数据
        normalized_df.insert(0, first_column.name, first_column.iloc[1:].reset_index(drop=True))

        # 保存归一化后的数据到输出目录
        normalized_df.to_csv(output_file, index=False)

        print(f"已处理并保存归一化文件: {csv_file}")

if __name__ == '__main__':
    preprocess_filtered_code_change_lines_sum()
    normalize_filtered_data()
