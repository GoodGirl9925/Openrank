# OpenTrustworthy——开源软件可信性评估与预测工具

## 背景分析

### 当下开源生态

### 痛点问题

## 项目成果

### 开源软件可信性评估模型

基于`ISO 9126`软件质量评价标准，为开源软件建立了一套可信性评估模型。具体来说，评估每一个开源软件的ABCD等可信属性和n个可信子属性，并通过xx模型yy算法，得出该软件的可信值（1到10之间）。

下表列出了可信属性、可信子属性，以及与之对应的开源项目指标。

#### 可用性 (Availability)

- **功能符合性 (Functionality Conformance)**
    
    - 无
- **功能准确性 (Accuracy of Functionality)**
    
    - 无
- **易理解性 (Understandability)**
    
    - 无
- **易操作性 (Operability)**
    
    - 无
- **适应性 (Adaptability)**
    
    - `openrank.json`
- **已安装性 (Installability)**
    
    - `stars.json`
    - `technical_fork.json`

#### 可靠性 (Reliability)

- **成熟性 (Maturity)**
    
    - `issues_closed.json`
- **容错性 (Fault Tolerance)**
    
    - 无

#### 安全性 (Security)

- **数据保密性 (Data Confidentiality)**
	- 无
- **代码安全性 (Code Security)**
    
    - `code_change_lines_sum.json`
- **控制保密性 (Control Confidentiality)**
    
    - 无

#### 实时性 (Timeliness)

- **时间特性 (Time Characteristics)**
    - `activity.json`
    - `attention.json`
    - `bus_factor.json`
    - `change_request_age.json`
    - `issue_age.json`
    - `participants.json`

#### 可维护性 (Maintainability)

- **易分析性 (Analyzability)**
    
	- `inactive_contributors.json`
    - `new_contributors.json`
- **可改变性 (Changeability)**
    
    - `code_change_lines_add.json`
    - `code_change_lines_remove.json`
- **稳定性 (Stability)**
    
    - `issues_and_change_request_active.json`
    - `issues_new.json`
- **易测试性 (Testability)**
    
    - `change_requests_reviews.json`

#### 可生存性 (Survivability)

- **抗攻击性 (Attack Resistance)**
    
    - 无
- **攻击识别性 (Attack Identification)**
    
    - 无
- **易恢复性 (Recoverability)**
    
    - `change_request_resolution_duration.json`
    - `issue_resolution_duration.json`
- **自我完善性 (Self-improvement)**
    
    - `change_request_response_time.json`
    - `issue_response_time.json`


结果格式：

```json
{
	"project_name_1":{
		"overall_trustworthy":{
			"date_1":value,
			"date_2":value,
			...
		},
		"attribute_trustworthy":{
			"date_1":{
				"availability":value,
				"reliability":value,
				"security":value,
				"timeliness":value,
				"maintainability":value,
				"survivability":value
			},
			"date_2":{},
			...
		},
		"subAttribute_trustworthy":{
			"date_1":{
				"availability":{
					"functionality_conformance":value,
					"accuracy_of_functionality":value,
					"understandability":value,
					"operability":value,
					"adaptability":value,
					"installability":value
				},
				"reliability":{
					"maturity":value,
					"fault_tolerance":value
				},
				"security":{
					"data_confidentiality":value,
					"code_security":value,
					"control_confidentiality":value
				},
				"timeliness":{
					"time_characteristics":value
				},
				"maintainability":{
					"analyzability":value,
					"changeability":value,
					"stability":value,
					"testability":value
				},
				"survivability":{
					"attack_resistance":value,
					"attack_identification":value,
					"recoverability":value,
					"self_improvement":value
				}
			},
			"date_2":{},
			...
		}
	},
	"project_name_2":{},
	...
}
```

### TOP300流行开源项目可信性可视化

分析前300流行项目指标数据`top300_metrics`，计算这些优秀的开源软件在各个可信属性上的得分以及总的软件可信值，并可视化。

### 基于机器学习的开源软件可信性预测

通过xx机器学习算法，拟合某一开源软件CHAOSS指标中的每一项，并估计未来半年该软件可信性、可信属性的变化。

### 开源软件可信性报告自动生成

基于大语言模型，为特定开源软件生成一份可信性报告，包括历史数据和未来预测。

## 代码详解

### 代码结构

