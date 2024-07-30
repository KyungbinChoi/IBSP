import numpy as np
import matplotlib.pyplot as plt

stds = []
ns = (10, 20, 30, 50, 70, 100, 200, 1000)
for n in ns:
    sample_means = []
    for _ in range(10000):
        samples = np.random.normal(0, 1 , n)
        sample_mean = np.mean(samples)
        sample_means.append(sample_mean)

    mean_std = np.std(sample_means)# code here
    stds.append(mean_std)

plt.plot(range(len(ns)), stds)
plt.xticks(range(len(ns)), ns, rotation=30)
plt.xlabel('The number of samples')
plt.ylabel('SD of sample mean')
plt.show()
