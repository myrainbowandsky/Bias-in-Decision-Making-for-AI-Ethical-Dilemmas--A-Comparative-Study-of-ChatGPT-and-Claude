import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

x_labels = [
    "8", "35", "70",
    "Masculine", "Feminine", "Androgynous",
    "Modest", "Stylish", "Luxury",
    "Black", "White", "Yellow",
    "Asian", "Caucasian", "African",
    "Good-looking", "Standard-looking", "Unpleasant-looking",
    "Disabled", "Non-disabled"
]

data = data1  # data1 is GPT's intersectional data

data_new1 = np.zeros_like(data, dtype=float)

# Normalization
for i, (x_category, x_indices) in enumerate(category_dict.items()):
    for j, (y_category, y_indices) in enumerate(category_dict.items()):
        sub_data = data[np.ix_(x_indices, y_indices)]
        sum_values = np.sum(sub_data)
        if sum_values > 0:
            normalized_sub_data = sub_data / sum_values
            data_new1[np.ix_(x_indices, y_indices)] = normalized_sub_data

# print(data_new1)

data = data2 # data2 is Claude's intersectional data
data_new2 = np.zeros_like(data, dtype=float)

# Normalization
for i, (x_category, x_indices) in enumerate(category_dict.items()):
    for j, (y_category, y_indices) in enumerate(category_dict.items()):
        sub_data = data[np.ix_(x_indices, y_indices)]
        sum_values = np.sum(sub_data)
        if sum_values > 0:
            normalized_sub_data = sub_data / sum_values
            data_new2[np.ix_(x_indices, y_indices)] = normalized_sub_data

data_new_filtered = np.where(data_new1 >= 0, data_new1, 0)
data_new_filtered_ = np.where(data_new2 >= 0, data_new2, 0)

data_new_filtered[:18] = data_new_filtered[:18] / 17
data_new_filtered_[:18] = data_new_filtered_[:18] / 17

data_new_filtered[18:] = data_new_filtered[18:] / 18
data_new_filtered_[18:] = data_new_filtered_[18:] / 18

mean_values_chatgpt = np.sum(data_new_filtered, axis=0)
mean_values_claude = np.sum(data_new_filtered_, axis=0)

combined_means = list(zip(x_labels, mean_values_chatgpt, mean_values_claude))

filtered_means = [(label, v1, v2) for (label, v1, v2) in combined_means if v1 > 0 or v2 > 0]

filtered_means.sort(key=lambda x: x[1], reverse=True)

sorted_labels, mean_values_chatgpt_sorted, mean_values_claude_sorted = zip(*filtered_means)

plt.figure(figsize=(12, 6))

bar_width = 0.35
x = np.arange(len(sorted_labels))

plt.bar(x, mean_values_chatgpt_sorted, color='#7e9bb7', label='GPT', alpha=0.5)

plt.xticks(rotation=45, ha='right', fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0, 0.5)
plt.legend(fontsize=30)

ax = plt.gca()
for spine in ax.spines.values():
    spine.set_color('#ffffff')

ax.set_facecolor('#ffffff')

plt.xticks(x, sorted_labels, rotation=45, ha='right', fontsize=20,weight='bold')
plt.yticks(fontsize = 20,weight = 'bold')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

bar_width = 0.35
x = np.arange(len(sorted_labels))
plt.bar(x, mean_values_claude_sorted, color='#f28e2b', label='Claude', alpha=0.5)
plt.xticks(rotation=45, ha='right', fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(0, 0.5)
plt.legend(fontsize=30)

ax = plt.gca()
for spine in ax.spines.values():
    spine.set_color('#ffffff')

ax.set_facecolor('#ffffff')

plt.xticks(x, sorted_labels, rotation=45, ha='right', fontsize=20,weight='bold')
plt.yticks(fontsize = 20,weight = 'bold')

plt.tight_layout()
plt.show()