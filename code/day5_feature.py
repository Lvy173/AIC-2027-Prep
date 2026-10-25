
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
CURRENT_DIR = Path(__file__).resolve().parent
DATA_PATH = CURRENT_DIR / 'train.csv'
print(f"=== 正在读取: {DATA_PATH} ===")
df = pd.read_csv(DATA_PATH)
bins = [0, 12, 18, 60, 100]
labels = ['Child','Teen','Adult','Senior']
df['AgeGroup'] = pd.cut(df['Age'],bins=bins,labels=labels)
survival_rate = df.groupby(['AgeGroup', 'Sex'], observed=False)['Survived'].mean().unstack()
print("\n=== 多维度生存统计 ===")
print(survival_rate)
survival_rate.plot(kind='bar',figsize=(8,5),color=['#4C72B0','#C44E52'])
plt.title('Surival Rate by Age Group and Sex')
plt.ylabel('Survival Rate')
plt.xlabel('Age Group')
plt.xticks(rotation=0)
plt.savefig(CURRENT_DIR / 'age_sex_survival_plot.png')
print("\n=== 高级图已保存为 age_sex_survival_plot.png ===")
plt.show()