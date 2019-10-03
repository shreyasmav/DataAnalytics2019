import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD

from sklearn import decomposition
from sklearn import datasets




########################   PCA   ####################################
np.random.seed(5)

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
X = iris.data
y = iris.target

fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)

for name, label in [('Setosa', 0), ('Versicolour', 1), ('Virginica', 2)]:
    ax.text3D(X[y == label, 0].mean(),
              X[y == label, 1].mean() + 1.5,
              X[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))

y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.nipy_spectral,
           edgecolor='k')

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

plt.show()



########################   SVD   ####################################



plt.style.use('ggplot')
plt.figure(figsize=(6, 5))
 
X = iris.data
y = iris.target

 
 
X_scaled = StandardScaler().fit_transform(X)
 
svd = TruncatedSVD(n_components=2)
Y_fitted = svd.fit_transform(X_scaled)



 
 
for labels, columns, name in [(0, 'black', 'Sentosa'), (1, 'blue','Versicolor'), (2, 'orange','Virginica')]:
    plt.scatter(Y_fitted[y==labels, 0],Y_fitted[y==labels, 1],label=name,c=columns,marker='*', s=50)
    
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(loc='best')
plt.title("SVD DATA ANALYSTICS", fontsize=20)
plt.show()

list(zip((0, 1, 2),('red', 'green', 'blue')))

[(0, 'black', 'Sentosa'), (1, 'violet','Versicolor'), (2, 'pink','Virginica')]

