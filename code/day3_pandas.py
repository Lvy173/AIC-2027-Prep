
import pandas as pd
df = pd.read_csv('code/train.csv')
print("=== 清洗前的缺失值 ===")
print(df.isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df.drop(columns=['Cabin'])
df = df.dropna()
print("\n=== 清洗后的缺失值 ===")
print(df.isnull().sum())
print("\n=== 数据形状 ===")
print(df.shape)