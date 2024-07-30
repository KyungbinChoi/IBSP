import numpy as np

def var_estimator(nums, ddof):
    '''
    ddof는 Delta Degrees of Freedom의 약자로, 감소된 자유도를 의미합니다.
    예컨대 분산을 구할 때 ddof=1이면 n-1을 자유도(분모)로 사용합니다.
    주어진 ddof를 이용하여 nums의 분산을 구하시오
    '''
    sample_variance = np.var(nums, ddof=ddof)
    return sample_variance 

def estimate_iterator(mu, sigma, n, ddof, n_iter):
    '''
    n_iterator 횟수만큼
    주어진 mu와 sigma를 따르는 정규분포에서 n개를 샘플링한 뒤
    추출된 샘플의 분산을, 주어진 ddof를 고려하여 계산한다.
    '''
    estimates = []
    for _ in range(n_iter):
        nums = np.random.normal(loc=mu, scale=sigma, size=n)
        estimate = var_estimator(nums, ddof)
        estimates.append(estimate)
    return estimates

def bias_reporter(mu, var, n, ddof, n_iter):
    '''
    주어진 ddof로 분산을 추정했을 때의 bias가 얼마나 되는지 구한다.
    '''
    estimates = estimate_iterator(mu, var, n, ddof, n_iter)
    biasses = np.array(estimates) - var
    mean_bias = np.mean(biasses)
    print(f'ddof = {ddof}일 때, 분산의 추정값은 평균적으로 {np.mean(estimates):.2f}')
    print(f'따라서 편향은 평균적으로 {mean_bias:.4f}\n')
    return mean_bias

def var_estimate_reporter(mu, var, n, n_iter):
    biasses = {}
    print(f'모 분산: {var**2}\n')
    for ddof in (0, 1):
        biasses[ddof] = bias_reporter(mu, var, n, ddof, n_iter)
    print(f'자유도를 n으로 했을 때의 편향은 자유도를 n-1로 했을 때보다 {abs(biasses[0] / biasses[1]):.2f}배 크다')

np.random.seed(85)
var_estimate_reporter(10, 5, 50, 100000)