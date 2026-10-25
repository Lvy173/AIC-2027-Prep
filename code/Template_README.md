# Day 3 数据处理任务

## 1. 任务说明

使用 `pandas` 对 Titanic 格式的数据进行基础清洗。处理流程为：使用均值填充 `Age` 缺失值，删除缺失较多的 `Cabin` 列，再删除仍然包含缺失值的记录。本练习用于掌握表格数据读取、缺失值检查和基础清洗方法。

## 2. 环境与依赖

- Python 3.9+
- pandas 1.5+

在仓库根目录安装依赖：

```powershell
python -m pip install -r teaching/submissions/S111777333/03-data-cleaning/requirements.txt
```

## 3. 文件说明

| 文件 | 类型 | 说明 |
| :--- | :--- | :--- |
| `day3_pandas.py` | 脚本 | 读取、检查并清洗数据 |
| `data/sample_train.csv` | 数据 | 为本任务编写的公开样例，不包含比赛原始数据 |
| `Day3.md` | 日志 | 实验日志与报错截图记录 |
| `README.md` | 文档 | 说明文件 |
| `requirements.txt` | 依赖 | Python 依赖范围 |

## 4. 运行方法与预期结果

在仓库根目录执行：

```powershell
python teaching/submissions/S111777333/03-data-cleaning/day3_pandas.py
```

程序默认读取脚本所在目录中的 `data/sample_train.csv`，不受终端当前目录影响。公开样例清洗后的数据形状为 `(7, 11)`，各列缺失值统计均为 0。

使用自己合法获取的完整 Titanic `train.csv` 时，将文件放入本任务的 `data` 目录，再执行：

```powershell
python teaching/submissions/S111777333/03-data-cleaning/day3_pandas.py --input teaching/submissions/S111777333/03-data-cleaning/data/train.csv
```

## 5. 数据来源与公开范围

仓库中的 `data/sample_train.csv` 是为验证清洗流程而编写的虚构样例，可以随本仓库公开。它只模仿 Titanic 训练集的字段结构，不包含真实乘客记录，也不是比赛数据。

完整数据可从 [Kaggle Titanic 竞赛数据页](https://www.kaggle.com/competitions/titanic/data) 由使用者自行获取。下载和使用前应阅读该页面的规则与数据条款。完整比赛数据未随本提交重新发布。

## 6. 已知范围与限制

- 使用均值填充 `Age` 忽略了年龄的分布特征，可能存在统计偏差。
- 直接删除 `Cabin` 列会损失潜在的有效信息。
- `dropna()` 会直接删除仍有缺失值的记录，正式项目中应先分析缺失原因和业务影响。
- 原始实验使用的完整数据从 891 行降至 889 行；该结果只对应日志中的完整数据，不是公开样例的预期行数。
