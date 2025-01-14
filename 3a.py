import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# num1 is GPT's single data and num2 is Claude's single data

categories_x = ['Age', 'Gender', 'Dressing', 'Color', 'Race', 'Look', 'Disability']

group_size = 3
groups = [num1[i:i + group_size] for i in range(0, len(num1), group_size)]
squared_diff_totals1 = [np.sum(group) for group in groups]

group_size = 3
groups = [num2[i:i + group_size] for i in range(0, len(num2), group_size)]
squared_diff_totals2 = [np.sum(group) for group in groups]

num1_shape = 1-np.array(squared_diff_totals1).reshape(1, 7)/50
num2_shape = 1-np.array(squared_diff_totals2).reshape(1, 7)/50

plt.figure(figsize=(12, 5))

values1 = num1_shape.flatten()
values2 = num2_shape.flatten()

i = 1 # 1 means sorted by GPT and 2 means sorted by Claude
if i == 1:
    combined_data = list(zip(values1, categories_x[:len(values1)]))
    combined_data_sorted = sorted(combined_data, key=lambda x: x[0], reverse=True)
    sorted_values1, sorted_labels = zip(*combined_data_sorted)
    sorted_values2 = [values2[categories_x.index(label)] for label in sorted_labels]
elif i == 2:
    combined_data = list(zip(values2, categories_x[:len(values2)]))
    combined_data_sorted = sorted(combined_data, key=lambda x: x[0], reverse=True)
    sorted_values2, sorted_labels = zip(*combined_data_sorted)
    sorted_values1 = [values1[categories_x.index(label)] for label in sorted_labels]
plt.figure(figsize=(12, 4))
bar1 = plt.bar(sorted_labels, sorted_values1,color='#7e9bb7',alpha=0.5,label='GPT')
bar2 = plt.bar(sorted_labels, sorted_values2,color='#f28e2b',alpha=0.5,label='Claude')

plt.xticks(fontsize = 20,weight='bold')
plt.yticks(fontsize = 20,weight='bold')
plt.legend(fontsize=30)  
plt.ylim(0, 1)  

ax = plt.gca()
ax.set_facecolor('#ffffff')

for spine in ax.spines.values():
    spine.set_color('#ffffff')

plt.tight_layout()
plt.show()
