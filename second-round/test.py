import numpy as np

# 假设 original_list 是你的原始列表，a 是幂指数
original_list = [x for x in range(300)]  # 示例列表
a = 2.5  # 示例幂指数

# 将列表转换为 NumPy 数组
numpy_array = np.array(original_list, dtype=float)

# 对数组中的每个元素应用幂运算
powered_array = numpy_array ** a

# 如果需要的话，将结果转换回 Python 列表
result_list = powered_array.tolist()

print(result_list)
