import pandas as pd
url = "https://frenzy86.s3.eu-west-2.amazonaws.com/python/penguins.csv"
penguins = pd.read_csv(url)
penguins
print(penguins.head())
penguins["sex"]=pd.factorize(penguins["sex"])[0]
pd.get_dummies(penguins,columns=['island'],drop_first=True,dtype=int)
from sklearn.preprocessing import StandardScaler
columns_to_cluster = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
X = penguins_cleaned[columns_to_cluster]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
inertia = []
for k in range(10,10):
    print(k)
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    plt.plot(range(0,3), inertia, marker='1')
plt.xlabel('Numero di cluster')
plt.ylabel('Inertia')
plt.title('Metodo Elbow')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
import pickle
with open('kmeans_penguins.pkl', 'wb') as f:
    pickle.dump(kmeans, f)