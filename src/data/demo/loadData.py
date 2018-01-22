# coding:UTF-8

import numpy as np
from src import App

"""演示从文本中加载数据"""

file_name = App.BASE_DATA + "/npl/affinity_dataset.txt"
x = np.loadtxt(file_name)

n_samples, n_features =x.shape
print("This dataset has {0} samples and {1} features".format(n_samples, n_features))

# The names of the features, for your reference.
features = ["bread", "milk", "cheese", "apples", "bananas"]

# First, how many rows contain our premise: that a person is buying apples
num_apple_purchases = 0
for sample in x:
    if sample[3] == 1:  # This person bought Apples
        num_apple_purchases += 1
print("{0} people bought Apples".format(num_apple_purchases))