"""
정규 분포로부터 추출한 샘플로부터 Bootstrap을 이용해 중앙값의 신뢰구간을 구해보고, 
실제 시뮬레이션을 통해 구한 중앙값의 분포를 비교
"""
import numpy as np

def chi_bootstrap_median_CI(df, n, bootstrap_count):
    samples = np.random.chisquare(df, n)

    medians = []
    for _ in range(bootstrap_count):
        bootstrap_sample = np.random.choice(samples, replace=False, size=n)
        bootstrap_median = np.median(bootstrap_sample)
        medians.append(bootstrap_median)
    # Bootstrap 중앙값의 표준 오차 계산
    se_median = np.std(medians)  # 표준 오차

    # Z값 (95% 신뢰수준)
    z_value = 1.96
    bootstrap_median = np.median(medians)  # 중앙값의 중앙값
    lower_bound = bootstrap_median - z_value * se_median  # 하한
    upper_bound = bootstrap_median + z_value * se_median  # 상한
    print(f"Bootstrap CI: ({lower_bound:.2f}, {upper_bound:.2f})")

def chi_median_distribution(df, n, sample_count):
    medians = []
    for _ in range(sample_count):
        samples = np.random.chisquare(df, n)
        sample_median = np.median(samples)
        medians.append(sample_median)
    se_median = np.std(medians)  # 표준 오차
    # Z값 (95% 신뢰수준)
    z_value = 1.96
    bootstrap_median = np.median(medians)  # 중앙값의 중앙값
    lower_bound = bootstrap_median - z_value * se_median  # 하한
    upper_bound = bootstrap_median + z_value * se_median  # 상한
    print(f"Sample CI: ({lower_bound:.2f}, {upper_bound:.2f})")


np.random.seed(85)

df = 23
n = 200
repeat_count = 10000

chi_bootstrap_median_CI(df, n, repeat_count)
chi_median_distribution(df, n, repeat_count)