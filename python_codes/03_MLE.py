#정규 분포로부터 추출한 샘플로부터 MLE를 도출하고 우도와 로그-우도를 사용하고 비교

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def likelihood_plotter(n, method):
    samples = np.sort(np.random.uniform(-1, 1, n))  # -1과 1 사이에서 n개 샘플링
    mu_likelihood = {}
    sigma = 1  # 표준 정규분포로 가정
    
    for mu in np.arange(-1, 1, 0.01):  # -1과 1 사이의 평균(mu)을 대상으로 계산
        if method == 'likelihood':
            # 우도 계산: 정규분포 PDF를 사용한 값의 곱 (전체 우도)
            likelihood = np.prod(norm.pdf(samples, loc=mu, scale=sigma))
            mu_likelihood[mu] = likelihood
        elif method == 'log-likelihood':
            # 로그 우도 계산: 정규분포 PDF의 로그를 더한 값
            log_likelihood = np.sum(np.log(norm.pdf(samples, loc=mu, scale=sigma)))
            mu_likelihood[mu] = log_likelihood

    # 그래프 그리기
    plt.plot(list(mu_likelihood.keys()), list(mu_likelihood.values()))
    plt.xlabel('mu')
    plt.ylabel(method)
    plt.title(f'{method} vs mu')
    plt.show()

# 예시 실행
likelihood_plotter(500, 'likelihood')

likelihood_plotter(1000, 'likelihood')

likelihood_plotter(500, 'log-likelihood')