import yaml
import numpy as np


# 根据指定的索引调整列表中m个元素的值，使得它们的和为1，同时将其他元素设为1
def adjust_list(nums, m_indices):
    # 计算调整比例，使选中的m个元素的和为1
    selected_sum = sum(nums[i] for i in m_indices)
    scale_factor = 1 / selected_sum

    # 调整选中的m个元素
    for i in m_indices:
        nums[i] *= scale_factor

    # 将其余元素设为1
    for i in range(len(nums)):
        if i not in m_indices:
            nums[i] = 1

    return nums


class Trustworthy:
    def __init__(self, yaml_path="weights.yaml"):
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        self.overall_weight = data.get('overall_weight')
        self.availability_weight = data.get('availability_weight')
        self.reliability_weight = data.get('reliability_weight')
        self.security_weight = data.get('security_weight')
        self.timeliness_weight = data.get('timeliness_weight')
        self.maintainability_weight = data.get('maintainability_weight')
        self.survivability_weight = data.get('survivability_weight')


    # 传入特定时间时，在各个可信子属性下，公司/项目的可信得分（一维向量，维数等于公司/项目的数量）
    def set_trustworthy_score(self, activity, attention, bus_factor, change_request_age,
                              change_request_resolution_duration, change_request_response_time,
                              change_requests_reviews, code_change_lines_add, code_change_lines_remove,
                              code_change_lines_sum, inactive_contributors, issue_age, issue_resolution_duration,
                              issue_response_time, issues_and_change_request_active,
                              issues_closed, issues_new, new_contributors, openrank,
                              participants, stars, technical_fork):
        self.activity = activity
        self.attention = attention
        self.bus_factor = bus_factor
        self.change_request_age = change_request_age
        self.change_request_resolution_duration = change_request_resolution_duration
        self.change_request_response_time = change_request_response_time
        self.change_requests_reviews = change_requests_reviews
        self.code_change_lines_add = code_change_lines_add
        self.code_change_lines_remove = code_change_lines_remove
        self.code_change_lines_sum = code_change_lines_sum
        self.inactive_contributors = inactive_contributors
        self.issue_age = issue_age
        self.issue_resolution_duration = issue_resolution_duration
        self.issue_response_time = issue_response_time
        self.issues_and_change_request_active = issues_and_change_request_active
        self.issues_closed = issues_closed
        self.issues_new = issues_new
        self.new_contributors = new_contributors
        self.openrank = openrank
        self.participants = participants
        self.stars = stars
        self.technical_fork = technical_fork


    # 计算可信子属性的值
    def calculate_subAttributes(self):
        # 对于负相关指标，取x = 10 - x
        # negative_metrics = [self.change_request_age, self.change_request_resolution_duration, self.change_request_reponse_time,
        #                     self.code_change_lines_sum, self.inactive_contributors, self.issue_age, self.issue_resolution_duration,
        #                     self.issue_response_time, self.issues_new]

        self.change_request_age = [10 - x for x in self.change_request_age]
        self.change_request_resolution_duration = [10 - x for x in self.change_request_resolution_duration]
        self.change_request_response_time = [10 - x for x in self.change_request_response_time]
        self.code_change_lines_sum = [10 - x for x in self.code_change_lines_sum]
        self.inactive_contributors = [10 - x for x in self.inactive_contributors]
        self.issue_age = [10 - x for x in self.issue_age]
        self.issue_resolution_duration = [10 - x for x in self.issue_resolution_duration]
        self.issue_response_time = [10 - x for x in self.issue_response_time]
        self.issue_new = [10 - x for x in self.issues_new]

        # adaptability
        self.subA_adaptability = self.openrank

        # installability
        lists_installability = [self.stars, self.technical_fork]
        self.subA_installability = [sum(values) / len(values) for values in zip(*lists_installability)]

        # maturity
        self.subA_maturity = self.issues_closed

        # code security
        self.subA_code_security = self.code_change_lines_sum

        # time characteristics
        lists_time_characteristics = [self.activity, self.attention, self.bus_factor,
                                      self.change_request_age, self.issue_age, self.participants]
        self.subA_time_characteristics = [sum(values) / len(values) for values in zip(*lists_time_characteristics)]

        # analyzability
        lists_analyzability = [self.inactive_contributors, self.new_contributors]
        self.subA_analyzability = [sum(values) / len(values) for values in zip(*lists_analyzability)]

        # changeability
        lists_changeability = [self.code_change_lines_add, self.code_change_lines_remove]
        self.subA_changeability = [sum(values) / len(values) for values in zip(*lists_changeability)]

        # stability
        lists_stability = [self.issues_and_change_request_active, self.issues_new]
        self.subA_stability = [sum(values) / len(values) for values in zip(*lists_stability)]

        # testability
        self.subA_testability = self.change_requests_reviews

        # recoverability
        lists_recoverability = [self.change_request_resolution_duration, self.issue_resolution_duration]
        self.subA_recoverability = [sum(values) / len(values) for values in zip(*lists_recoverability)]

        # self-improvement
        lists_self_improvement = [self.change_request_response_time, self.issue_response_time]
        self.subA_self_improvement = [sum(values) / len(values) for values in zip(*lists_self_improvement)]

        # print("self.subA_adaptability:", self.subA_adaptability)
        # print("self.subA_installability:", self.subA_installability)
        # print("self.subA_maturity:", self.subA_maturity)
        # print("self.subA_code_security:", self.subA_code_security)
        # print("self.subA_time_characteristics:", self.subA_time_characteristics)
        # print("self.subA_analyzability:", self.subA_analyzability)
        # print("self.subA_changeability:", self.subA_changeability)
        # print("self.subA_stability:", self.subA_stability)
        # print("self.subA_testability:", self.subA_testability)
        # print("self.subA_recoverability:", self.subA_recoverability)
        # print("self.subA_self_improvement:", self.subA_self_improvement)


    # 计算可信属性的值
    def calculate_attributes(self):
        # availability
        non_empty_subA_availability = [4, 5]
        self.availability_weight = adjust_list(self.availability_weight, non_empty_subA_availability)
        pow_subA_adaptability = np.array(self.subA_adaptability, dtype=float) ** self.availability_weight[4]
        pow_subA_installability = np.array(self.subA_installability, dtype=float) ** self.availability_weight[5]
        self.attr_availability = (pow_subA_adaptability * pow_subA_installability).tolist()

        # reliability
        non_empty_subA_reliability = [0]
        self.reliability_weight = adjust_list(self.reliability_weight, non_empty_subA_reliability)
        pow_subA_issues_closed = np.array(self.subA_maturity, dtype=float) ** self.reliability_weight[0]
        self.attr_reliability = pow_subA_issues_closed.tolist()

        # security
        non_empty_subA_security = [1]
        self.security_weight = adjust_list(self.security_weight, non_empty_subA_security)
        pow_subA_code_change_lines_sum = np.array(self.subA_code_security, dtype=float) ** self.security_weight[1]
        self.attr_security = pow_subA_code_change_lines_sum.tolist()

        # timeliness
        non_empty_subA_timeliness = [0]
        self.timeliness_weight = adjust_list(self.timeliness_weight, non_empty_subA_timeliness)
        pow_subA_issues_closed = np.array(self.subA_time_characteristics, dtype=float) ** self.timeliness_weight[0]
        self.attr_timeliness = pow_subA_issues_closed.tolist()

        # maintainability
        non_empty_subA_maintainability = [0, 1, 2, 3]
        self.maintainability_weight = adjust_list(self.maintainability_weight, non_empty_subA_maintainability)
        pow_subA_analyzability = np.array(self.subA_analyzability, dtype=float) ** self.maintainability_weight[0]
        pow_subA_changeability = np.array(self.subA_changeability, dtype=float) ** self.maintainability_weight[1]
        pow_subA_stability = np.array(self.subA_stability, dtype=float) ** self.maintainability_weight[2]
        pow_subA_testability = np.array(self.subA_testability, dtype=float) ** self.maintainability_weight[3]
        self.attr_maintainability = (pow_subA_analyzability * pow_subA_changeability * pow_subA_stability * pow_subA_testability).tolist()

        # survivability
        non_empty_subA_survivability = [2, 3]
        self.survivability_weight = adjust_list(self.survivability_weight, non_empty_subA_survivability)
        pow_subA_recoverability = np.array(self.subA_recoverability, dtype=float) ** self.survivability_weight[2]
        pow_subA_self_improvement = np.array(self.subA_self_improvement, dtype=float) ** self.survivability_weight[3]
        self.attr_survivability = (pow_subA_recoverability * pow_subA_self_improvement).tolist()

        # print("self.attr_availability:", self.attr_availability)
        # print("self.attr_reliability:", self.attr_reliability)
        # print("self.attr_security:", self.attr_security)
        # print("self.attr_timeliness:", self.attr_timeliness)
        # print("self.attr_maintainability:", self.attr_maintainability)
        # print("self.attr_survivability:", self.attr_survivability)


    # 计算总的软件可信值
    def calculate_overall_trustworthy(self):
        pow_attr_availability = np.array(self.attr_availability, dtype=float) ** self.overall_weight[0]
        pow_attr_reliability = np.array(self.attr_reliability, dtype=float) ** self.overall_weight[1]
        pow_attr_security = np.array(self.attr_security, dtype=float) ** self.overall_weight[2]
        pow_attr_timeliness = np.array(self.attr_timeliness, dtype=float) ** self.overall_weight[3]
        pow_attr_maintainability = np.array(self.attr_maintainability, dtype=float) ** self.overall_weight[4]
        pow_attr_survivability = np.array(self.attr_survivability, dtype=float) ** self.overall_weight[5]
        self.overall_trustworthy = (pow_attr_availability * pow_attr_reliability * pow_attr_security *
                                    pow_attr_timeliness * pow_attr_maintainability * pow_attr_survivability).tolist()

        # print("self.overall_trustworthy:", self.overall_trustworthy)


    # 可信度量值，返回格式为数值
    def get_overall_trustworthy(self, project_index):
        # print(self.overall_trustworthy)
        return self.overall_trustworthy[project_index]


    # 可信属性值，返回格式为字典：{}
    def get_attribute_trustworthy(self, project_index):
        attribute_trustworthy = {}
        attribute_trustworthy['availability'] = self.attr_availability[project_index]
        attribute_trustworthy['reliability'] = self.attr_reliability[project_index]
        attribute_trustworthy['security'] = self.attr_security[project_index]
        attribute_trustworthy['timeliness'] = self.attr_timeliness[project_index]
        attribute_trustworthy['maintainability'] = self.attr_maintainability[project_index]
        attribute_trustworthy['survivability'] = self.attr_survivability[project_index]

        return attribute_trustworthy

    # 可信子属性值，返回格式为字典：{}
    def get_subAttribute_trustworthy(self, project_index):
        subAttribute_trustworthy = {}
        subAttribute_trustworthy['availability'] = {}
        subAttribute_trustworthy['reliability'] = {}
        subAttribute_trustworthy['security'] = {}
        subAttribute_trustworthy['timeliness'] = {}
        subAttribute_trustworthy['maintainability'] = {}
        subAttribute_trustworthy['survivability'] = {}

        subAttribute_trustworthy['availability']['functionality_conformance'] = None
        subAttribute_trustworthy['availability']['accuracy_of_functionality'] = None
        subAttribute_trustworthy['availability']['understandability'] = None
        subAttribute_trustworthy['availability']['operability'] = None
        subAttribute_trustworthy['availability']['adaptability'] = self.subA_adaptability[project_index]
        subAttribute_trustworthy['availability']['installability'] = self.subA_installability[project_index]

        subAttribute_trustworthy['reliability']['maturity'] = self.subA_maturity[project_index]
        subAttribute_trustworthy['reliability']['fault_tolerance'] = None

        subAttribute_trustworthy['security']['data_confidentiality'] = None
        subAttribute_trustworthy['security']['code_security'] = self.subA_code_security[project_index]
        subAttribute_trustworthy['security']['control_confidentiality'] = None

        subAttribute_trustworthy['timeliness']['time_characteristics'] = self.subA_time_characteristics[project_index]

        subAttribute_trustworthy['maintainability']['analyzability'] = self.subA_analyzability[project_index]
        subAttribute_trustworthy['maintainability']['changeability'] = self.subA_changeability[project_index]
        subAttribute_trustworthy['maintainability']['stability'] = self.subA_stability[project_index]
        subAttribute_trustworthy['maintainability']['testability'] = self.subA_testability[project_index]

        subAttribute_trustworthy['survivability']['attack_resistance'] = None
        subAttribute_trustworthy['survivability']['attack_identification'] = None
        subAttribute_trustworthy['survivability']['recoverability'] = self.subA_recoverability[project_index]
        subAttribute_trustworthy['survivability']['self_improvement'] = self.subA_self_improvement[project_index]

        return subAttribute_trustworthy

