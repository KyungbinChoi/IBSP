import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson

def norm_cdf_drawer(mu, sigma):
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
    y = norm.cdf(x, mu, sigma)
    
    plt.plot(x, y, label=f'N({mu}, {sigma}^2)')
    plt.title('Normal Distribution CDF')
    plt.xlabel('x')
    plt.ylabel('CDF')
    plt.legend()
    plt.grid(True)
    plt.show()

def poisson_cdf_drawer(lamb):
    x = np.arange(0, 2*lamb + 1)
    y = poisson.cdf(x, lamb)
    
    plt.plot(x, y, 'bo-', label=f'Poisson($\lambda$={lamb})')
    plt.title('Poisson Distribution CDF')
    plt.xlabel('x')
    plt.ylabel('CDF')
    plt.legend()
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    norm_cdf_drawer(7, 3)
    poisson_cdf_drawer(3)
    poisson_cdf_drawer(10)
