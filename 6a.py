import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# num1 is GPT's single data and num2 is Claude's single data

x_labels = [
    "8", "35", "70",
    "Masculine", "Feminine", "Androgynous",
    "Modest", "Stylish", "Luxury",
    "Black", "White", "Yellow",
    "Asian", "Caucasian", "African",
    "Good-looking", "Standard-looking", "Unpleasant-looking",
    "Disabled", "Non-disabled"
]

gapd = 0 # Center value

# Calculate (GPT-Claude)/(GPT+Claude)
shap = (np.array(num1) - np.array(num2))/(np.array(num1) + np.array(num2))
shap = np.nan_to_num(shap)
shap_abs = np.abs(shap)
# print(shap)

df = pd.DataFrame({
    'Feature': x_labels,
    'shap': shap,
    'abs shap': shap_abs
})

# Sort by shap
df = df.sort_values(by='shap', ascending=True)

df = df[np.abs(df['shap']) >= gapd]

df['shap'] = np.where(df['shap'] >= 0, df['shap'] - gapd, df['shap'] + gapd)

plt.figure(figsize=(10, 6))
ax = plt.gca()

for i, row in df.iterrows():
    if row['shap'] >= 0:
        # GPT > Claude
        plt.barh(row['Feature'], row['shap'], color='#7e9bb7',alpha=0.5, edgecolor=None)
    else:
        # Claude > ChatGPT
        plt.barh(row['Feature'], row['shap'], color='#f28e2e',alpha=0.5, edgecolor=None)

plt.legend(handles=[
    plt.Line2D([0], [0], color='#7e9bb7',alpha=0.5, lw=14, label='GPT'),
    plt.Line2D([0], [0], color='#f28e2e',alpha=0.5, lw=14, label='Claude')
],fontsize=20)

plt.xlim(- 1+gapd, 1-gapd)  

ax.set_xticks(np.arange(-(1-gapd), (1.1-gapd), 0.5))
ax.set_xticklabels([str(round(i)/10+gapd) for i in range(-round((1-gapd)*10), round((1.1-gapd)*10), 5)])
plt.xticks(fontsize = 18,weight='bold')
plt.yticks(fontsize = 18,weight='bold')

for spine in ax.spines.values():
    spine.set_color('#ffffff')
ax.set_facecolor('#ffffff')

plt.tight_layout()
plt.show()
