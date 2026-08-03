# Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import openpyxl
import seaborn as sns


# Path to file
path = "E:\isolated_FB.xlsx"
os.path.exists(path)
df = pd.read_excel(path)


labels = ['200_concentrated', 'Homogenised']

fig, ax = plt.subplots(figsize=(8, 6))

sns.boxplot(
    data=df,
    x="Condition_protocol",
    y="N_clumps",
    boxprops=dict(facecolor="cyan", alpha=0.2),
    medianprops=dict(color="black"),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
    fliersize=0,
    ax=ax
)

sns.scatterplot(
    data=df,
    x="Condition_protocol",
    y="N_clumps",
    color="black",
    s=40,
    zorder=3,
    ax=ax
)

plt.title('N° of clumps per conditions')
plt.show()




cell_type = ['Spore', 'VC']
subset = df[
    (df['Condition_protocol']=='Homogenised') &
    (df['Object_type'].notna())
    ]

fig, ax = plt.subplots(figsize=(8, 6))

sns.boxplot(
    data=subset,
    x="Object_type",
    y="Manual_count_objects",
    boxprops=dict(facecolor="cyan", alpha=0.2),
    medianprops=dict(color="black"),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
    fliersize=0,
    ax=ax
)

sns.scatterplot(
    data=subset,
    x="Object_type",
    y="Manual_count_objects",
    color="black",
    s=40,
    zorder=3,
    ax=ax
)
plt.title('N° Objects - condition homogenised')
plt.show()