import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# data1 is GPT's intersectional data and data2 is Claude's intersectional data

category_dict = {
    'Age': [0, 1, 2],
    'Sex': [3, 4, 5],
    'Dressing': [6, 7, 8],
    'Color': [9, 10, 11],
    'Race': [12, 13, 14],
    'Look': [15, 16,17],
    'Healthy': [18, 19]
}

categories_x = ['Age', 'Gender', 'Dressing', 'Color', 'Race', 'Look', 'Disability']

def process_data(data, num_categories):
    data_less = np.zeros((num_categories, num_categories))

    for i, (x_category, x_indices) in enumerate(category_dict.items()):
        for j, (y_category, y_indices) in enumerate(category_dict.items()):
            sub_data = data[np.ix_(x_indices, y_indices)]
            sum_values = np.sum(sub_data)
            data_less[i, j] = 1 - sum_values / 50

    return np.sum(data_less, axis=0)/6

data_less_t1 = process_data(data1, len(category_dict))
data_less_t2 = process_data(data2, len(category_dict))

values1 = data_less_t1.reshape(1, -1)
values2 = data_less_t2.reshape(1, -1)

i = 1 # 1 means sorted by GPT and 2 means sorted by Claude

if i == 1:
    combined_data = list(zip(values1.flatten(), categories_x[:len(values1.flatten())]))
    combined_data_sorted = sorted(combined_data, key=lambda x: x[0], reverse=True)
    sorted_values1, sorted_labels = zip(*combined_data_sorted)
    sorted_values2 = [values2.flatten()[categories_x.index(label)] for label in sorted_labels]
elif i == 2:
    combined_data = list(zip(values2.flatten(), categories_x[:len(values2.flatten())]))
    combined_data_sorted = sorted(combined_data, key=lambda x: x[0], reverse=True)
    sorted_values2, sorted_labels = zip(*combined_data_sorted)
    sorted_values1 = [values1.flatten()[categories_x.index(label)] for label in sorted_labels]

plt.figure(figsize=(12, 4))
indices = np.arange(len(sorted_labels))

bar1 = plt.bar(indices, sorted_values1, color='#7e9bb7', alpha=0.5, label='GPT')
bar2 = plt.bar(indices, sorted_values2, color='#f28e2b', alpha=0.5, label='Claude')

plt.xticks(indices, sorted_labels, fontsize=20, weight='bold')
plt.yticks(fontsize=20, weight='bold')

plt.legend(fontsize=30)
plt.ylim(0, 1)

ax = plt.gca()
ax.set_facecolor('#ffffff')
for spine in ax.spines.values():
    spine.set_color('#ffffff')

plt.tight_layout()
plt.show()
