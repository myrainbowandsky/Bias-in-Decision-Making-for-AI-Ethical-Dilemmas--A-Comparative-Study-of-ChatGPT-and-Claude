import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_std = data_std1 # data_std1 is GPT's standard deviation and data_std2 is Claude's standard deviation

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

data_peak = np.zeros((len(category_dict), len(category_dict)))

for i, (x_category, x_indices) in enumerate(category_dict.items()):
    for j, (y_category, y_indices) in enumerate(category_dict.items()):
        sub_data = data_std[np.ix_(x_indices, y_indices)]
        peak_sum_values = np.sum(abs(sub_data))
        data_peak[i, j] = peak_sum_values
        if i == j:
            data_peak[i, j] = 0

num1_shape = np.sum(data_peak, axis=1) / 6

data_std = data_std2

data_peak = np.zeros((len(category_dict), len(category_dict)))

for i, (x_category, x_indices) in enumerate(category_dict.items()):
    for j, (y_category, y_indices) in enumerate(category_dict.items()):
        sub_data = data_std[np.ix_(x_indices, y_indices)]
        peak_sum_values = np.sum(abs(sub_data))
        data_peak[i, j] = peak_sum_values
        if i == j:
            data_peak[i, j] = 0

num2_shape = np.sum(data_peak, axis=1) / 6

total_shape = num1_shape + num2_shape

combined_data = list(zip(total_shape, categories_x[:len(total_shape)]))
combined_data_sorted = sorted(combined_data, key=lambda x: x[0])

sorted_totals, sorted_labels = zip(*combined_data_sorted)

sorted_values1 = [num1_shape[categories_x.index(label)] for label in sorted_labels]
sorted_values2 = [num2_shape[categories_x.index(label)] for label in sorted_labels]

plt.figure(figsize=(12, 4))

bar1 = plt.bar(sorted_labels, sorted_values1, color='#7e9bb7',alpha=0.5, label='GPT')
bar2 = plt.bar(sorted_labels, sorted_values2, bottom=sorted_values1, color='#f28e2b',alpha=0.5, label='Claude')

plt.xticks(fontsize=20, weight='bold')
plt.yticks(fontsize=20, weight='bold')

plt.legend(fontsize=30, loc='upper left')

plt.ylim(0,1)

ax = plt.gca()
ax.set_facecolor('#ffffff')

for spine in ax.spines.values():
    spine.set_color('#ffffff')

plt.tight_layout()
plt.show()
