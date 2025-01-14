import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

category_dict = {
    'Age': [0, 1, 2],
    'Sex': [3, 4, 5],
    'Dressing': [6, 7, 8],
    'Color': [9, 10, 11],
    'Race': [12, 13, 14],
    'Look': [15, 16,17],
    'Disability': [18, 19]
}

categories_x = ['Age', 'Gender', 'Dressing', 'Color', 'Race', 'Look', 'Disability']

data = data1 # data1 is GPT's intersectional data and data2 is Claude's intersectional data

data_new = np.zeros_like(data, dtype=float)

data_less = np.zeros((len(category_dict), len(category_dict)))

# Normalization
for i, (x_category, x_indices) in enumerate(category_dict.items()):
    for j, (y_category, y_indices) in enumerate(category_dict.items()):
        sub_data = data[np.ix_(x_indices, y_indices)]
        sum_values = np.sum(sub_data)
        data_less[i, j] = 50-sum_values
        if sum_values > 0:
            normalized_sub_data = sub_data / sum_values
            data_new[np.ix_(x_indices, y_indices)] = normalized_sub_data

plt.figure(figsize=(15, 12))
ax=sns.heatmap(data_new, cmap='viridis', annot=False,xticklabels=False,yticklabels=False,vmin = 0,vmax=1)

ax.xaxis.tick_top()

for i in range(0, data_new.shape[0] + 1, 3):
    ax.axhline(i, color='gray', linestyle='--', linewidth=1)

for j in range(0, data_new.shape[1] + 1, 3):
    ax.axvline(j, color='gray', linestyle='--', linewidth=1)

for category, indices in category_dict.items():
    for i in indices:
        for j in indices:
            data_new[i,j]=-1
            rect = plt.Rectangle((j, i), 1, 1, color='#8dcec8', alpha=1)
            ax.add_patch(rect)

for i in range(data_new.shape[0]):
    for j in range(data_new.shape[1]):
        if data_new[i, j] > 0.5: # Frequencies greater than 0.5 are marked to two decimals
            plt.text(j + 0.5, i + 0.5, int(data_new[i,j]*100)/100, color='black', fontsize=12, ha='center', va='center',weight='bold')

category_positions_x = [(1.5, 'black'), (4.5, 'black'), (7.5, 'black'), (10.5, 'black'), (13.5, 'black'), (16.5, 'black'), (19, 'black')]
category_positions_y = [(1.9, 'black'), (4.9, 'black'), (8.2, 'black'), (11, 'black'), (14, 'black'), (17, 'black'), (20, 'black')]


for idx, (pos, color) in enumerate(category_positions_x):
    plt.text(pos, -0.3, categories_x[idx], color=color, fontsize=18, weight='bold', ha='center')

for idx, (pos, color) in enumerate(category_positions_y):
    plt.text(-0.5, pos, categories_x[idx], color=color, fontsize=18, weight='bold', ha='center',rotation=90)

plt.tick_params(axis='x',pad=25)
plt.tick_params(axis='y',pad=25)

plt.xticks(rotation=45,ha='left',fontsize = 23)
plt.yticks(fontsize = 23)

colorbar = ax.collections[0].colorbar
colorbar.ax.tick_params(labelsize=25)

plt.show()
