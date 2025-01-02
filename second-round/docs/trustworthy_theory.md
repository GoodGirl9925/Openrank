# 软件可信度量模型公式

## 模型1

$$ T_1 = \frac{10}{11}\left(\frac{y_{\text{min}}}{10}\right)^\epsilon y^{\alpha_1}_1 y^{\alpha_2}_2 \cdots y^{\alpha_m}_m + \frac{10}{11} y^{\beta_{m+1}}_{m+1} y^{\beta_{m+2}}_{m+2} \cdots y^{\beta_{m+s}}_{m+s} $$

- $0 \leq \epsilon \leq 1 - \alpha_{\text{min}}$ 控制最小关键属性对软件可信度的影响。
- $1 \leq y_i \leq 10, 1 \leq i \leq m+s$ 是每个属性的值范围。
- $y_{\text{min}} = \min\{y_i | i=1, \cdots, m\}$ 是所有关键属性中的最小值。

## 模型2

$$ T_2 = \frac{10}{11}\left(\frac{y_{\text{min}}}{10}\right)^\epsilon y^{\alpha_1}_1 y^{\alpha_2}_2 \cdots y^{\alpha_m}_m + \frac{10}{11} y^{\beta_{i'}}_{\text{min}'} $$

- $y_{\text{min}'} = \min\{y_j | m+1 \leq j \leq m+s\}$ 是所有非关键属性中的最小值。

## 模型3

$$ T_3 = \left[\alpha\left(\min_{1\leq i\leq m}\left\{\left(\frac{1}{y_{0i}}\right)^\epsilon y^{\alpha_1}_1 y^{\alpha_2}_2 \cdots y^{\alpha_m}_m\right\}\right)^{-\rho} + \beta\left(y^{\beta_{m+1}}_{m+1} y^{\beta_{m+2}}_{m+2} \cdots y^{\beta_{m+s}}_{m+s}\right)^{-\rho}\right]^{-\frac{1}{\rho}} $$

- $0 \leq \epsilon \leq \min\{1 - \alpha_{\text{min}}', \frac{\ln y_0 - \ln y'_{\text{min}}}{\ln y'_{\text{min}} - \ln 10}\}$
- $1 \leq y_0 \leq y_i \leq 10, 1 \leq i \leq m+s$

## 数学性质验证

对于上述三个模型，我们验证了它们满足以下性质：

- **非负性**：$T \geq 0$
- **归一化**：$1 \leq T \leq 10$
- **单调性**：$\frac{\partial T}{\partial y_i} \geq 0$
- **加速性**：$\frac{\partial^2 T}{\partial y^2_i} \leq 0$
- **敏感性**：$\delta_i = \frac{\partial T / \partial y_i}{T / y_i} \geq 0$
- **替代性**：$\sigma_{ij} = \frac{d(\frac{y_i}{y_j})}{d(h_{ij})} \cdot \frac{h_{ij}}{\frac{y_i}{y_j}}$
- **界值性**：$y_0 \leq T \leq \max\{y_1, \cdots, y_{m+s}\}$，其中 $y_0$ 是一个基准值。