# Day 6 数据处理任务：数据分布分析与环境隔离

## 1. 任务说明
对 Titanic 数据进行年龄分布分析，绘制直方图，并配置环境依赖文件。

## 2. 环境与依赖
- pandas 1.5+
- matplotlib 3.5+
在根目录执行安装依赖：
`python -m pip install -r teaching/submissions/S111777333/06-data-distribution/requirements.txt`

## 3. 文件说明
| 文件 | 说明 |
| :--- | :--- |
| `day6_distribution.py` | 分布分析主程序 |
| `data/sample_train.csv` | 脱敏测试样本 |
| `age_distribution_plot.png` | 生成的年龄分布直方图 |

## 4. 运行方法与预期结果
在根目录执行：
`python teaching/submissions/S111777333/06-data-distribution/day6_distribution.py`
预期结果：生成 `age_distribution_plot.png`，无 `plt.show()`。

## 5. 已知范围与限制
使用相对绝对路径自动定位数据。图表基于 20 行小样本，仅作代码流程验证，不代表全量真实数据的绝对业务结论。