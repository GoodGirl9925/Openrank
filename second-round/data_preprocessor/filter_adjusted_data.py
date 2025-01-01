import os
import pandas as pd

def filter_adjusted_data():
    # 设置文件夹路径
    input_folder = '../data/adjusted_data/'
    output_folder = '../data/filtered_data/'

    # 如果输出目录不存在，创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取所有CSV文件名
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    # 初始化一个字典来存储每个文件的公司名集合
    company_sets = {}

    # 读取每个文件并获取公司名列（假设第一列是公司名）
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        df = pd.read_csv(file_path)
        company_names = set(df['Company'].values)  # 获取公司名列
        company_sets[csv_file] = company_names

    # 找出所有文件中公司名的交集
    common_companies = set.intersection(*company_sets.values())

    # 依次处理每个CSV文件
    for csv_file in csv_files:
        file_path = os.path.join(input_folder, csv_file)
        df = pd.read_csv(file_path)

        # 过滤掉不在交集中的公司
        filtered_df = df[df['Company'].isin(common_companies)]

        # 生成新的文件名
        new_file_name = 'filtered' + csv_file[len('adjusted'):]

        # 保存处理后的文件到输出文件夹
        output_file_path = os.path.join(output_folder, new_file_name)
        filtered_df.to_csv(output_file_path, index=False)

    print("处理完成！所有文件已保存到:", output_folder)

if __name__ == '__main__':
    filter_adjusted_data()
