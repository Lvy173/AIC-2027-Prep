import numpy as np
img = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print("原始图像的shape(形状):", img.shape)
crop = img[0:2, 0:2]
print("裁剪后的区域:\n",crop)
matrix_a = np.random.rand(2, 3)
matrix_b = np.random.rand(3, 4)
print("矩形A的形状:",matrix_a. shape)
print("矩形B的形状:",matrix_b. shape)
result = np.dot(matrix_a,matrix_b)
print("乘法结果矩阵的形状:",result.shape)