import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

data = data1 # data1 is GPT's intersectional data and data2 is Claude's intersectional data

category_dict = {
    'Age': [0, 1, 2],
    'Sex': [3, 4, 5],
    'Dressing': [6, 7, 8],
    'Color': [9, 10, 11],
    'Race': [12, 13, 14],
    'Look': [15, 16,17],
    'Healthy': [18, 19]
}

data_new = np.zeros_like(data, dtype=float)

for i, (x_category, x_indices) in enumerate(category_dict.items()):
    for j, (y_category, y_indices) in enumerate(category_dict.items()):
        sub_data = data[np.ix_(x_indices, y_indices)]
        sum_values = np.sum(sub_data)
        if sum_values > 0:
            normalized_sub_data = sub_data / sum_values
            data_new[np.ix_(x_indices, y_indices)] = normalized_sub_data

feature_names = ["8", "35", "70", "Masculine", "Feminine", "Androgynous", 
                 "Modest", "Stylish", "Luxury", "Black", "White", "Yellow", 
                 "Asian", "Caucasian", "African", "Good-looking", 
                 "Standard-looking", "Unpleasant-looking", "Disabled", "Non-disabled"]

data = data_new

results = pd.DataFrame(data, columns=feature_names)
results['Cluster'] = feature_names

linked = linkage(data, 'ward')

plt.figure(figsize=(12, 6))

def get_link_color(link):
    return '#f28e2b'

dendrogram(linked, orientation='top', labels=feature_names, distance_sort='descending',
           show_leaf_counts=True, link_color_func=get_link_color)

ax = plt.gca()
plt.xticks(fontsize=20, weight='bold', rotation=45, ha='right')
plt.yticks(fontsize=18, weight='bold')

for spine in ax.spines.values():
    spine.set_color('#ffffff')
ax.set_facecolor('#ffffff')

plt.tight_layout()
plt.show()
