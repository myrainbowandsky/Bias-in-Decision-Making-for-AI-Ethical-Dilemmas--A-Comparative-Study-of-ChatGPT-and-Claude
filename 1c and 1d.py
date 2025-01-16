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

x_labels = [
    "8", "35", "70",
    "Masculine", "Feminine", "Androgynous",
    "Modest", "Stylish", "Luxury",
    "Black", "White", "Yellow",
    "Asian", "Caucasian", "African",
    "Good-looking", "Standard-looking", "Unpleasant-looking",
    "Disabled", "Non-disabled"
]

data = data1 # data1 is GPT's intersectional data and data2 is Claude's intersectional data

data_new = np.zeros_like(data, dtype=float)

# Normalization
for i, (x_category, x_indices) in enumerate(category_dict.items()):
    for j, (y_category, y_indices) in enumerate(category_dict.items()):
        sub_data = data[np.ix_(x_indices, y_indices)]
        sum_values = np.sum(sub_data)
        if sum_values > 0:
            normalized_sub_data = sub_data / sum_values
            data_new[np.ix_(x_indices, y_indices)] = normalized_sub_data

flat_data = data_new.flatten()
indices = np.arange(flat_data.size)
sorted_indices = np.argsort(flat_data)[::-1]

top_indices = sorted_indices[:20:2] # 20 indicates top 10

label_set = []
top_values = []

y_labels = x_labels

for idx in top_indices:
    x_index = idx % data_new.shape[1]
    y_index = idx // data_new.shape[1]
    value = flat_data[idx]
    label_set.append((x_labels[x_index], y_labels[y_index]))
    top_values.append(value)

combined_labels = [f"{x},{y}" for (x, y) in label_set]

plt.figure(figsize=(10, 6))

ax=sns.barplot(y=combined_labels, x=top_values[:len(combined_labels)*2:1], color='#7e9bb7',alpha = 0.5)

plt.xlim(0, 1.1)

for index, value in enumerate(top_values[:len(combined_labels)]):
    ax.text(value+0.01, index, f'{value:.3f}', va='center',color='black',weight = 'bold',fontsize = 20)

ax.set_facecolor('#ffffff')

for spine in ax.spines.values():
    spine.set_color('#ffffff')

plt.xticks(fontsize=25,weight = 'bold')
plt.yticks(fontsize=25,weight = 'bold')

plt.show()
