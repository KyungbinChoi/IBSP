import numpy as np
import matplotlib.pyplot as plt

domestic_prices = [9800, 7490, 4480, 3750, 12900, 7480, 11900, 16500, 10620, 7900, 10900, 19500, 8900, 4800, 9900, 34900, 33000, 15000, 49000, 13500, 7950, 8415, 8000, 5500, 7110, 12900, 12160, 8640, 3950, 5480, 6900, 25900, 15800, 6500, 5650, 5980, 10625, 19800, 5600, 29750, 15210, 8820, 9405, 10500, 8850, 7553, 9900, 8980, 19000, 15000, 8000, 3750, 13000, 9900, 5850, 18905, 10000, 39000, 12350, 14400, 45000, 11305, 24900, 11353, 7553, 2975, 11900, 12800, 10500, 7900, 6950, 8500, 2800, 4200, 3500, 6900, 2750, 8500, 5800, 9900, 37000, 13110, 9900, 8900, 29665, 4800, 11950]
imported_prices = [2030, 2280, 750, 8800, 4950, 3200, 2700, 3200, 3800, 7950, 5940, 3300, 11900, 3900, 4700, 4500, 2080, 1350, 1170, 4500, 2160, 8500, 4580, 10900, 8900, 6980, 3900, 5400, 5300, 4500, 4800, 16500, 13500, 4400, 4400, 2660, 39900, 6200, 8700, 1650, 7950, 2900, 3500, 2900, 6950, 6950, 2800, 3500, 6900, 9900, 8500, 14900, 9900, 21000]

total_price_mean = np.mean(domestic_prices+imported_prices)
total_price_std = np.std(domestic_prices+imported_prices)
print(f"전체 과일의 가격 평균: {total_price_mean:.2f}")
print(f"전체 과일의 가격 표준 편차: {total_price_std:.2f}\n")

domestic_price_mean = np.mean(domestic_prices)
domestic_price_std = np.std(domestic_prices)
print(f"국산 과일의 가격 평균: {domestic_price_mean:.2f}")
print(f"국산 과일의 가격 표준 편차: {domestic_price_std:.2f}\n")

imported_price_mean = np.mean(imported_prices)
imported_price_std = np.std(imported_prices)
print(f"수입 과일의 가격 평균: {imported_price_mean:.2f}")
print(f"수입 과일의 가격 표준 편차: {imported_price_std:.2f}\n")

plt.figure(figsize=(12,6))
plt.hist(domestic_prices+imported_prices, bins=10, density=True, alpha=0.9,color='blue',label='total price')
plt.hist(domestic_prices, bins=10, density=True, alpha=0.9,color='red',label='domestic price')
plt.hist(imported_prices, bins=10, density=True, alpha=0.9,color='green',label='imported price')
plt.show()
