from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris() # 데이터 꺼내기
X = pd.DataFrame(iris.data, columns = iris['feature_names']) # pandas df로 변환

sepal_length = X['sepal length (cm)']
sepal_length_normalized = (sepal_length - sepal_length.min()) / (sepal_length.max() - sepal_length.min())
sepal_length_standarized = (sepal_length - sepal_length.mean()) / sepal_length.std()

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(15,5))
ax1.hist(sepal_length, color='skyblue')
ax1.set_title('Original')
ax2.hist(sepal_length_normalized, color='skyblue')
ax2.set_title('Normalization')
ax3.hist(sepal_length_standarized, color='skyblue')
ax3.set_title('Standardization')
plt.show()
