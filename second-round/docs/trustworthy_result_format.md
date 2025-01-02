# 软件可信值计算结果格式

在`second-round/data/trustworthy_data`文件目录中，软件可信值计算的结果`trustworthy_origin.json`和`trustworthy_filtered.json`，都遵循如下格式：

```json
{
    "project_name_1": {
        "overall_trustworthy": {
            "date_1": value,
            "date_2": value
            //...
        },
        "attribute_trustworthy": {
            "date_1": {
                "availability": value,
                "reliability": value,
                "security": value,
                "timeliness": value,
                "maintainability": value,
                "survivability": value
            },
            "date_2": {}
            //...
        },
        "subAttribute_trustworthy": {
            "date_1": {
                "availability": {
                    "functionality_conformance": value,
                    "accuracy_of_functionality": value,
                    "understandability": value,
                    "operability": value,
                    "adaptability": value,
                    "installability": value
                },
                "reliability": {
                    "maturity": value,
                    "fault_tolerance": value
                },
                "security": {
                    "data_confidentiality": value,
                    "code_security": value,
                    "control_confidentiality": value
                },
                "timeliness": {
                    "time_characteristics": value
                },
                "maintainability": {
                    "analyzability": value,
                    "changeability": value,
                    "stability": value,
                    "testability": value
                },
                "survivability": {
                    "attack_resistance": value,
                    "attack_identification": value,
                    "recoverability": value,
                    "self_improvement": value
                }
            },
            "date_2": {}
            //...
        }
    },
    "project_name_2": {}
    //...
}
```
