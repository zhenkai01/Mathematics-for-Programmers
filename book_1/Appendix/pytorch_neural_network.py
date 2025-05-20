import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# 生成一些数据
n_samples = 100
data = torch.randn(n_samples, 2)
labels = (data[:, 0]**2 + data[:,1]**2 < 1).float().unsqueeze(1)

#可视化数据
plt.scatter(data[:, 0], data[:, 1], c=labels.squeeze(), cmap='coolwarm')
plt.title("Generated Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()