import numpy as np
def normal_sample_comparison(n, mu, sigma):
    '''
    정규 분포으로부터 n개의 샘플을 난수 추출한 뒤, 표본 평균과 분산을 실제 모수와 비교해보자
    '''
    samples = np.random.normal(loc=mu, scale=sigma, size=n)

    sample_mean = samples.mean()
    sample_sigma = samples.std()

    print(f"Norm({mu}, {sigma}^2)의 표본 평균: {sample_mean:.2f}")
    print(f"Norm({mu}, {sigma}^2)의 표본 표준편차: {sample_sigma:.2f}")


if __name__ == "__main__":
    np.random.seed(85) 

    normal_sample_comparison(100, 50, 3)
    normal_sample_comparison(10, 20, 7)
    normal_sample_comparison(10000, 0, 100)
