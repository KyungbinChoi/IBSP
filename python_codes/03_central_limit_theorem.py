import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

def chi_mean_distribution(df, n):
    sample_means = []
    for _ in range(n):
        samples = np.random.chisquare(df, 10) # code here 10개의 샘플 추출
        sample_mean = np.mean(samples)# code here
        sample_means.append(sample_mean)
    xs = np.arange(0, df*3, 0.1)
    ps = [chi2.pdf(x, df) for x in xs]
    plt.hist(sample_means, density=True, bins=50)
    plt.plot(xs, ps)
    plt.legend([f'chi-squared(df={df})', 'sample mean'])
    plt.show()
    plt.show()


chi_mean_distribution(1, 100000)
chi_mean_distribution(3, 100000)
