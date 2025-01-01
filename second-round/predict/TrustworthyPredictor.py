import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


class XGBoostPredictor:
    def __init__(self):
        # 初始化模型
        self.models = [xgb.XGBRegressor(objective='reg:squarederror', booster='gbtree') for _ in range(7)]
        self.scalers = [MinMaxScaler(feature_range=(1, 10)) for _ in range(7)]  # 用于数据归一化
        self.seq_in = None
        self.seq_out = None

    def set_origin_seq(self, seq_in):
        """
        设置原始输入数据
        :param seq_in: 二维列表，维度为7*27
        """
        self.seq_in = np.array(seq_in)
        # 将数据归一化到[1, 10]区间
        for i in range(7):
            self.seq_in[i] = self.scalers[i].fit_transform(self.seq_in[i].reshape(-1, 1)).flatten()

    def _prepare_data(self):
        """
        准备训练数据：从现有的27个月数据中提取特征和标签
        使用滚动窗口来准备数据，window_size = 6
        """
        window_size = 6
        X = []
        y = []
        for i in range(window_size, len(self.seq_in[0]) - 1):  # 从第6个月到第26个月，预测第27个月
            X.append(self.seq_in[:, i - window_size:i].flatten())  # 使用前6个月的数据作为特征
            y.append(self.seq_in[:, i + 1])  # 第27个月的真实值作为标签
        return np.array(X), np.array(y)

    def _train_model(self):
        """
        训练XGBoost模型：分别为总可信值和6个可信属性训练独立的模型
        """
        X, y = self._prepare_data()

        # 将每个属性单独进行训练
        for i in range(7):
            # 使用当前属性的数据作为y
            y_attr = y[:, i]
            self.models[i].fit(X, y_attr)

    def _predict_future(self):
        """
        预测未来9个月的数据，并确保结果在[1, 10]范围内
        """
        # 从2023-01到2023-03的数据进行预测
        seq_in_future = self.seq_in[:, -6:]  # 取最后6个月的数据进行预测
        future_X = []
        for i in range(7):
            future_X.append(seq_in_future.flatten())
            # 预测下一个月
            future_preds = np.array([model.predict(future_X[-1].reshape(1, -1)) for model in self.models])
            future_preds = np.clip(future_preds, 1, 10)  # 限制预测值在[1, 10]范围内
            future_X[-1] = future_preds.flatten()  # 更新特征数据
            seq_in_future = np.hstack([seq_in_future[:, 1:], future_preds.reshape(-1, 1)])  # 更新输入数据

        # 反归一化预测值
        future_preds_final = []
        for i in range(7):
            future_preds_final.append(self.scalers[i].inverse_transform(future_X[i].reshape(-1, 1)))

        self.seq_out = np.array(future_preds_final).T

    def get_predicted_seq(self):
        """
        获取预测的未来9个月数据
        :return: 预测结果，维度为7*9
        """
        if self.seq_in is None:
            raise ValueError("Input data not set. Please use set_origin_seq() to set the input data.")

        self._train_model()
        self._predict_future()

        return self.seq_out[0]


# test
if __name__ == '__main__':
    seq_in = [
        [8, 7.5, 7.6, 7.8, 7.9, 8.1, 8.3, 8.4, 8.6, 8.5, 8.4, 8.2, 8.1, 8.0, 8.2, 8.3, 8.5, 8.7, 8.8, 8.9, 8.9, 9.0, 9.0,
         9.1, 9.2, 9.3, 9.4],
        [7, 6.5, 6.8, 7.0, 7.2, 7.5, 7.6, 7.7, 7.8, 7.9, 7.8, 7.6, 7.5, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2,
         8.3, 8.4, 8.5, 8.6],
        [6, 5.5, 5.8, 6.0, 6.2, 6.4, 6.5, 6.6, 6.7, 6.8, 6.7, 6.6, 6.5, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2,
         7.3, 7.4, 7.5, 7.6],
        [7.5, 7.0, 7.2, 7.3, 7.5, 7.7, 7.8, 8.0, 8.1, 8.2, 8.1, 8.0, 7.9, 7.8, 7.9, 8.0, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8,
         8.9, 9.0, 9.1, 9.2],
        [6.8, 6.3, 6.6, 6.7, 6.9, 7.0, 7.2, 7.3, 7.5, 7.6, 7.5, 7.4, 7.3, 7.1, 7.2, 7.3, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1,
         8.2, 8.3, 8.4, 8.5],
        [9, 8.7, 8.8, 9.0, 9.1, 9.3, 9.4, 9.5, 9.6, 9.7, 9.6, 9.5, 9.4, 9.3, 9.4, 9.5, 9.7, 9.8, 9.9, 10, 10, 10, 10, 10,
         10, 10, 10],
        [6, 5.5, 7.7, 7.8, 7.9, 7.8, 6.5, 6.6, 6.9, 7.0, 7.2, 7.3, 7.5, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2,
         7.3, 7.4, 7.5, 7.6]
    ]

    predictor = XGBoostPredictor()
    predictor.set_origin_seq(seq_in)
    predicted_seq = predictor.get_predicted_seq()

    print(predicted_seq)