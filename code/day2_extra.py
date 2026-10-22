
import numpy as np
data = np.array([1,2,3,4,5,6])
print("原始形状:", data.shape)
data_2x3 = data.reshape(2, 3)
print("\n变成2x3的矩阵:\n", data_2x3)
data_3x2 = data.reshape(3, 2)
print("\n变成3x2 的矩阵:\n",data_3x2)
result = np.dot(data_2x3,data_3x2)
print("\n2x3乘以 3x2 的结果:\n",result)
print("结果的形状:",result.shape)