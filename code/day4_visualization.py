
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
CURRENT_DIR = Path(__file__).resolve().parent
DATA_PATH = CURRENT_DIR / 'train.csv'
def visualize_data(data_path):
    print(f"===正在读取文件: {data_path} ===")
    df = pd.read_csv(data_path)
    df['Sex'] = df['Sex'].map({'male':0,'female':1})
    survival_rate = df.groupby('Sex')['Survived'].mean()
    plt.figure(figsize=(6,4))
    plt.bar(['Male(0)','Female(1)'],survival_rate.values, color=['#4C72B0','#C44E52'])
    plt.title('Titanic Survival Rate by Sex')
    plt.ylabel('Survival Rate')
    plt.savefig(CURRENT_DIR / 'survival_plot.png')
    print("\n=== 图表已保存为 survival_plot.png ===")
    plt.show()
if __name__ == "__main__":
    visualize_data(DATA_PATH)