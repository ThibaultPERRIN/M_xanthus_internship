# Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import openpyxl
import seaborn as sns


# Path-to-file
path = r'C:/Users/nmassoulie/Desktop/Thibault/FB_homogenisation_conditions_count.xlsx'
os.path.exists(path)

# Dataset
df = pd.read_excel(path)

# Subset from dataset
plot = df[['Amplitude', 'Pulse', 'Time', 'N_objects']]
# plot.sort_values(by=['Pulse'])

# Fig skeleton
fig = plt.figure(figsize=(20, 10))
subfigs = fig.subfigures(nrows=1, ncols=3, wspace=-0.1, width_ratios=[2, 0.5, 0.5])

# subfig amplitude skeleton
times = [15, 30]
amplitudes = [20, 25, 28]

axs = subfigs[0].subplots(
    nrows=len(times),
    ncols=len(amplitudes),
    sharey=True
)

# subfig_left
for i, time in enumerate(times):
    
    for j, amp in enumerate(amplitudes):
        
        ax = axs[i, j]
        
        # Condition
        if time == 15 and amp == 28:
            ax.set_axis_off()
            continue
        
        # Data
        subset = df[
            (df['Time'] == time) & (df['Amplitude'] == amp)
            ]
        
        # Boxplot
        bp = sns.boxplot(
            data=subset,
            x="Pulse",
            y="N_objects",
            ax=ax,
            boxprops=dict(facecolor="cyan", alpha=0.2),
            medianprops=dict(color="black"),
            whiskerprops=dict(color="black"),
            capprops=dict(color="black"),
            fliersize=0
        )
        
        # Scatterplot
        sns.scatterplot(
            data=subset,
            x="Pulse",
            y="N_objects",
            ax=ax,
            color="black",
            s=40,
            zorder=3
        )

        # Set axis title
        if j == 0:
            ax.set_ylabel("N objects")
            ax.text(
                -0.23, 0.5,
                f"{time} s",
                transform=ax.transAxes,
                rotation=90,
                ha="center",
                va="center",
                fontsize=12,
                fontweight='semibold',
                # color='darkblue'
            )

        if i == len(times) - 1:
            ax.set_xlabel("Pulse")
            ax.text(
                0.5, -0.2,
                f"Amplitude {amp}",
                transform=ax.transAxes,
                ha="center",
                va="top",
                fontsize=12,
                fontstyle='italic',
                fontweight='semibold',
                # color='darkblue'
            )
        
        # Axis margin-layout
        ax.margins(x=0.1)
        ax.set_yticks(np.arange(0, 450, 50))
        ax.grid(True)

# ax.set_title('Amplitude conditions')
# subfigs[0].suptitle(
#     "Amplitude conditions",
#     fontsize=16,
#     fontweight="bold"
# )

# subfig control
control = 0

subset_control = df[
    (df['Time'] == control) & (df['Amplitude'] == control)
]

ax_control = subfigs[1].subplots()

sns.boxplot(
    data=subset_control,
    x="Pulse",
    y="N_objects",
    ax=ax_control,
    boxprops=dict(facecolor="grey", alpha=0.2),
    medianprops=dict(color="black"),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
    fliersize=0
)

# Scatterplot
sns.scatterplot(
    data=subset_control,
    x="Pulse",
    y="N_objects",
    ax=ax_control,
    color="black",
    s=40,
    zorder=3
)




# ax_control.set_title("Control")
# subfigs[1].suptitle(
#     "Control",
#     fontsize=16,
#     fontweight="bold"
# )
ax_control.set_ylabel("N objects")
ax_control.text(
    1.8, -0.2,
    "∅ sonication",
    transform=ax.transAxes,
    ha="center",
    va="top",
    fontsize=12,
    fontstyle='italic',
    fontweight='semibold',
    # color='darkblue'
)
ax_control.grid(True)
ax_control.margins(x=0.3)




fig.suptitle("Homogenisation conditions", fontsize=25)

fig.text(
    0.34, 0.90,
    "Amplitude conditions",
    ha="center",
    fontsize=18,
)

fig.text(
    0.80, 0.90,
    "Control",
    ha="center",
    fontsize=18,
)


plt.show()


# Subfig clusters


# ax_clusters = subfigs[2].subplots()

# for i, time in enumerate(times):
    
#     for j, amp in enumerate(amplitudes):
        
        