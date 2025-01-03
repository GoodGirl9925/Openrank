# OpenTrustworthy——开源软件可信性评估与预测工具安装指南

## Install

首先进入项目目录，创建`conda`虚拟环境（推荐）：

```bash
    cd path/to/Openrank
    conda create -n opentrust python=3.10 -y
    conda activate opentrust
```

然后安装相关依赖：

```bash
  pip install -r requirements.txt
```

接着进入复赛文件目录：

```bash
  cd second-round
```

最后运行批处理文件：

- 对于`Linux/MacOS`系统：

```bash
    chmod +x run_project.sh
    ./run_project.sh
```

- 对于`Windows`系统：

```bash
  ./run_project.bat
```

