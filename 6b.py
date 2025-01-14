import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data1 is GPT's intersectional data and data2 is Claude's intersectional data

gapd = 0 # Center value

x_labels = [
    "8", "35", "70",
    "Masculine", "Feminine", "Androgynous",
    "Modest", "Stylish", "Luxury",
    "Black", "White", "Yellow",
    "Asian", "Caucasian", "African",
    "Good-looking", "Standard-looking", "Unpleasant-looking",
    "Disabled", "Non-disabled"
]

# Standard normalization factor
theta = np.array([17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,18,18])

means_chatgpt = np.sum(data1, axis=0)/theta
means_claude = np.sum(data2, axis=0)/theta

# Calculate (GPT-Claude)/(GPT+Claude)
shap = (means_chatgpt - means_claude)/(means_chatgpt + means_claude)
shap_abs = np.abs(shap)

df = pd.DataFrame({
    'Feature': x_labels,
    'Difference': shap,
    'Absolute Difference': shap_abs
})

# Sort by shap
df = df.sort_values(by='Difference', ascending=True)

plt.figure(figsize=(10, 6))
ax = plt.gca()  

for i, row in df.iterrows():
    if row['Difference'] >= 0:
        # GPT > Claude
        plt.barh(row['Feature'], row['Difference'], color='#7e9bb7',alpha = 0.5, edgecolor=None, label='GPT > Claude' if i == 0 else "")
    else:
        # Claude > ChatGPT
        plt.barh(row['Feature'], row['Difference'], color='#f28e2e',alpha = 0.5, edgecolor=None, label='Claude > GPT' if i == len(df)-1 else "")

plt.legend(handles=[
    plt.Line2D([0], [0], color='#7e9bb7',alpha = 0.5, lw=14, label='GPT'),
    plt.Line2D([0], [0], color='#f28e2e',alpha = 0.5, lw=14, label='Claude')
],fontsize=20)
plt.xticks(fontsize=18,weight='bold')
plt.yticks(fontsize=18,weight='bold')
plt.xlim(-1, 1)
ax.set_xticks(np.arange(-1,1.1,0.5)) # Note the extra 0.1 on the right
ax.set_xticklabels([str((i/10)) for i in range(-10,11,5)])

for spine in ax.spines.values():
    spine.set_color('#ffffff')
ax.set_facecolor('#ffffff')

plt.tight_layout()
plt.show()
