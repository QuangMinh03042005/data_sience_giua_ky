import collections
import os
import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("./shopping_trends.csv")
# print(data.head())
# print("max age: ",max(data["Age"]))
# print("max purchase amout: ", max(data["Purchase Amount (USD)"]))
# print("mean age: ", np.mean(data["Age"]))
# print("mean purchase amount: ", np.mean(data["Purchase Amount (USD)"]))
# print("----\n")


x = data["Age"]
y = data["Purchase Amount (USD)"]

# def myFunc(x):
#     return x >= 50

# mymodel = list(filter(myFunc, x))


plt.scatter(x, y)
# plt.plot(x, mymodel)
plt.ylim(ymin=0, ymax=200)
plt.xlim(xmin=0, xmax=100)
plt.xlabel("Age")
plt.ylabel ("Purchase amount")
plt.show()

# Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


# print(data.describe())
# print(set(data["Age"]))
# print(set(data["Item Purchased"]))
os.system("cls")
# print(data.iloc[0])
# print(data.iloc[0]["Age"])
# print(data.shape)

item = data["Item Purchased"]

counts = collections.Counter(item)
print(len(counts))
mc = counts.most_common(None)
print(mc)
print(max(mc, key=lambda x: x[1]))
