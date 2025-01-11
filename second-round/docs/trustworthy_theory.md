# OpenTrustworthy理论部分：国防科技大学软件可信度量模型

## 度量性质

**软件可信性的7个度量性质**：

**非负性**：软件的可信性度量值$T$必须是非负的。  
$$
T \geq 0
$$

**比例合适性**：各可信属性值$y_i$应该有合适的比例，确保软件可信性的量化能够真实反映用户的认同度，避免某些属性值过高或过低导致可信性度量失真。  
$$
\exists c_1, c_2 \in \Re^+ \quad \text{使得} \quad c_1 \leq \frac{y_i}{y_j} \leq c_2 \quad \text{其中} \quad 1 \leq i, j \leq m
$$

**单调性**：可信性度量函数 $T$ 应随着每个可信属性 $y_i$ 的增加而单调递增。
$$
\frac{\partial T}{\partial y_i} \geq 0
$$

**凝聚性**：凝聚性描述了一个属性的变化率。当只有一个属性 $y_i$ 增加而其他属性保持不变时，使用该属性的效率会逐渐降低。  
$$
\frac{\partial^2 T}{\partial y_i^2} \leq 0
$$

**灵敏性**：灵敏性$\delta_i$描述了可信属性值的变化对软件可信性的影响程度。灵敏性越高，属性值的变化对可信性的影响越大。  
$$
\delta_i = \frac{\frac{\partial T}{\partial y_i}}{\frac{T}{y_i}} = \frac{\frac{\partial T}{\partial y_i} \cdot y_i}{T} > 0
$$

**代替性**：代替性描述了在保持软件可信性不变的前提下，两个可信属性值之间的相互替代关系。即一个属性值的增加可以通过另一个属性值的减少来补偿。  
$$
\frac{\partial T}{\partial y_i} dy_i + \frac{\partial T}{\partial y_j} dy_j = 0
$$
$$
h_{ij} = -\frac{\frac{\partial T}{\partial y_j}}{\frac{\partial T}{\partial y_i}} = \frac{dy_i}{dy_j}
$$
其中，$h_{ij}$ 表示在软件可信性不变的情况下，增加（或减少）一个单位 $y_j$ 需要减少（或增加）多少个单位 $y_i$。

**可期望性**：如果所有可信属性都达到用户的预期，则软件的可信性也应满足用户的预期，并且可信性值不应超过最大可信属性值。  
$$
y_0 \leq \min\{y_1, \cdots, y_m\} \quad \text{推出} \quad y_0 \leq T \leq \max\{y_1, \cdots, y_m\}
$$
其中，$y_0$ 是用户对所有可信属性的最低预期值。

## 可信度量模型

**不区分关键属性和非关键属性**：

**模型0：**

$$
T_0 = y_1^{\alpha_1} y_2^{\alpha_2} \cdots y_m^{\alpha_m}
$$ 
其中要求 $1 \leq y_i \leq 10 (i = 1, \ldots, m)$，$\alpha_i$ 是可信属性 $y_i$ 的权重，满足性质 
(1) $0 < \alpha_i < 1$。 
(2) $\sum_{i=1}^{m} \alpha_i = 1$。

**区分关键属性和非关键属性**：

**模型1**：
  
$$ T_1 = \frac{10}{11}\left(\frac{y_{\text{min}}}{10}\right)^\epsilon y^{\alpha_1}_1 y^{\alpha_2}_2 \cdots y^{\alpha_m}_m + \frac{10}{11} y^{\beta_{m+1}}_{m+1} y^{\beta_{m+2}}_{m+2} \cdots y^{\beta_{m+s}}_{m+s} $$  
- $0 \leq \epsilon \leq 1 - \alpha_{\text{min}}$ 控制最小关键属性对软件可信度的影响。  
- $1 \leq y_i \leq 10, 1 \leq i \leq m+s$ 是每个属性的值范围。  
- $y_{\text{min}} = \min\{y_i | i=1, \cdots, m\}$ 是所有关键属性中的最小值。  
  
**模型2：**
  
$$ T_2 = \frac{10}{11}\left(\frac{y_{\text{min}}}{10}\right)^\epsilon y^{\alpha_1}_1 y^{\alpha_2}_2 \cdots y^{\alpha_m}_m + \frac{10}{11} y^{\beta_{i'}}_{\text{min}'} $$  
- $y_{\text{min}'} = \min\{y_j | m+1 \leq j \leq m+s\}$ 是所有非关键属性中的最小值。  
  
**模型3**：
  
$$ T_3 = \left[\alpha\left(\min_{1\leq i\leq m}\left\{\left(\frac{1}{y_{0i}}\right)^\epsilon y^{\alpha_1}_1 y^{\alpha_2}_2 \cdots y^{\alpha_m}_m\right\}\right)^{-\rho} + \beta\left(y^{\beta_{m+1}}_{m+1} y^{\beta_{m+2}}_{m+2} \cdots y^{\beta_{m+s}}_{m+s}\right)^{-\rho}\right]^{-\frac{1}{\rho}} $$

- $\epsilon$： 调控参数，用来调控最小关键属性对软件可信性的影响，满足 $0 \leq \epsilon \leq \min\{1 - \alpha_{\text{min}}', \frac{\ln y_0 - \ln y_{\text{min}}'}{\ln y_{\text{min}}' - \ln 10}\}$，且$\epsilon$越大，影响越大，$\alpha_{\text{min}}'$ 表示最小关键属性在整个关键属性集中所占的权重；
- $y_0$：由用户提供的可信属性值需达到的阈值；
- $\rho$：与关键属性和非关键属性之间替代性相关的参数，满足 $0 < \rho$，且其值越大，则关键属性与非关键属性间替代性越难；
- $y_i$：第$i(1 \leq i \leq m + s)$个可信属性的可信值，满足 $1 \leq y_0 \leq y_i \leq 10$。

## 可信属性度量模型

**模型1**：
$$ y_1 = x_1^{\gamma_1} x_2^{\gamma_2} \cdots x_n^{\gamma_n} $$

**模型2**：
$$ y_2 = \left( \sum_{i=1}^n \omega_i x_i^{-\rho_y} \right)^{-\frac{1}{\rho_y}}, \quad 1 \leq i \leq n, \quad 1 \leq x_i \leq 10 $$
- $\rho_y$：与可信属性$y$相匹配的参数，它是构成可信属性$y$的可信子属性间替代性相关的参数，满足$\rho_y > 0$，且其值越大，则可信子属性间替代性越难。
- $\omega_i$：可信属性$y$的可信子属性$x_i \, (1 \leq i \leq n)$权重，满足 $$ \sum_{i=1}^n \omega_i = 1, \quad 0 \leq \omega_i \leq 1. $$
