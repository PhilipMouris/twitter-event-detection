from scipy.cluster.hierarchy import average, dendrogram, fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
import joblib

dist = joblib.load('cosine.pkl')

linkage_matrix = average(dist)

c, coph_dists = cophenet(linkage_matrix, pdist(dist))

joblib.dump(linkage_matrix, 'cluster_average.pkl')

print(c)

fig, ax = plt.subplots(figsize=(15, 20))
ax = dendrogram(linkage_matrix, orientation="right");

plt.tick_params(\
    axis= 'x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')

plt.tight_layout()

plt.savefig('tweet_clusters.png', dpi=200)

plt.close()

clusters = fcluster(linkage_matrix, 5, criterion='maxclust')

clusters_list = clusters.tolist()
print(len(clusters_list))
output = {
    "cluster_labels": clusters_list
}

with open("cluster_labels.json", "w", encoding="utf8") as outfile:
    json.dump(output, outfile, indent=4, ensure_ascii=False)
