import numpy as np
from scipy import stats

def poisson_3m_calculator(lamb, n):

    samples = np.random.poisson(lamb, n)

    sample_mean = np.mean(samples)
    sample_median = np.median(samples)
    sample_mode =stats.mode(samples)

    print(f"표본 평균: {sample_mean:.2f}")
    print(f"표본 중앙값: {sample_median}")
    print(f"표본 최빈값: {sample_mode.mode[0]}")


np.random.seed(85)
poisson_3m_calculator(7, 100000)
