
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Day 6 数据分布分析")
parser.add_argument("--input", type=str, default=str(Path(__file__).resolve().parent / "data/sample_train.csv"),help="输入数据路径")
args = parser.parse_args()
DATA_PATH = Path(args.input)

print(f"=== 正在读取: {DATA_PATH} ===")
df = pd.read_csv(DATA_PATH)

df = df.dropna(subset=['Age'])

CURRENT_DIR = Path(__file__).resolve().parent
plt.figure(figsize=(8,5))
plt.hist(df['Age'], bins=10, color='#4C72B0', edgecolor='black', alpha=0.7)

plt.title('Titanic Passenger Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.savefig(CURRENT_DIR / 'age_distribution_plot.png')
print("\n=== 年龄分布图已保存为 age_distribution_plot.png ===")

