import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("D:\MPSTME\padhai\SEMESTER4\DWM\project\Mall_Customers.csv")

print(data.head())
print("Dataset shape:", data.shape)

print(data.isnull().any().any())

x = data.loc[:, ['Annual Income (k$)',
                 'Spending Score (1-100)']].values

print(x.shape)

from sklearn.neighbors import NearestNeighbors # importing the library
neighb = NearestNeighbors(n_neighbors=9) # creating an object of the NearestNeighbors class
nbrs=neighb.fit(x) # fitting the data to the object
distances,indices=nbrs.kneighbors(x) # finding the nearest neighbours

# Sort and plot the distances results
distances = np.sort(distances, axis = 0) # sorting the distances
distances = distances[:, 1] # taking the second column of the sorted distances
plt.rcParams['figure.figsize'] = (5,3) # setting the figure size
plt.plot(distances) # plotting the distances
plt.show() # showing the plot


from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps = 8, min_samples = 10).fit(x)


labels = dbscan.labels_ # getting the labels

print(labels)
# Plot the clusters
plt.scatter(x[:, 0], x[:,1], c = labels, cmap= "plasma") # plotting the clusters
plt.xlabel("Income") # X-axis label
plt.ylabel("Spending Score") # Y-axis label
plt.show() # showing the plot






#compare and contrast also 





