# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 11:08:06 2025

@author: bowen
"""
import pandas as pd
import os
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('default')

# Specify the directory and file name
filepath = "data/raw_data/LichenMossdata.xlsx"   # change this to your directory


# Load the Excel file into a DataFrame
df = pd.read_excel(filepath)

# Convert each column into a list
datalists = [df[col].tolist() for col in df.columns]

#separate data into variables 
sample = np.array(datalists[0])
aspect = np.array(datalists[9])
solar = np.array(datalists[10])
totcover = np.array(datalists[3])
mosscover = np.array(datalists[4])
angle = np.array(datalists[1])
elevation = np.array(datalists[11])

#calculate solar radiation times aspect
solspect = np.array(solar)*np.array(aspect)

# Plot total cover vs aspect
plt.figure(dpi=300)
plt.figure(figsize=(8, 4))
plt.grid(alpha=0.3)
plt.scatter(aspect, totcover, 20, c='maroon')
plt.title(f'Total cover versus aspect')
plt.xlabel('Aspect (° away from N)')
plt.ylabel('Total moss & lichen cover (%)')
# Add index labels next to each point
for i, (x, y) in enumerate(zip(aspect, totcover)):
    plt.text(
        x, y, sample[i],           # label with index
        fontsize=8,
        color='black',          # visible on black background
        ha='center', va='bottom'  # position relative to point
    )
plt.show()

# # Plot solar * aspect
# plt.figure(dpi=300)
# plt.figure(figsize=(8, 4))
# plt.grid(alpha=0.3)
# plt.scatter(solspect, totcover, 20, c='maroon')
# plt.title(f'Total cover versus solar radiation * aspect')
# plt.xlabel('Aspect (° away from N) * Solar radiation')
# plt.ylabel('Total moss & lichen cover (%)')
# # Add index labels next to each point
# for i, (x, y) in enumerate(zip(solspect, totcover)):
#     plt.text(
#         x, y, sample[i],           # label with index
#         fontsize=8,
#         color='black',          # visible on black background
#         ha='center', va='bottom'  # position relative to point
#     )
# plt.show()
 
# Plot total cover vs angle
plt.figure(dpi=300)
plt.figure(figsize=(8, 4))
plt.grid(alpha=0.3)
plt.scatter(angle, totcover, 20, c='maroon')
plt.title(f'Total cover versus angle')
plt.xlabel('Angle (° away from vertical)')
plt.ylabel('Total moss & lichen cover (%)')
plt.show()




#plot using additional variable with a colorbar

#plt.style.use('dark_background')
plt.figure(dpi=300, figsize=(8, 4))

# # Set background to black
# plt.rcParams['axes.facecolor'] = 'black'
# plt.rcParams['figure.facecolor'] = 'black'

# Create the scatter plot
scatter = plt.scatter(
    aspect,
    totcover,
    c=elevation,                 # color gradient based on angle
    cmap='viridis',          # choose a color map (e.g. 'plasma', 'coolwarm', 'inferno')
    s=20,                    # point size
    alpha=0.9
)

# Add colorbar to show angle gradient
cbar = plt.colorbar(scatter)
cbar.set_label('Elevation')

# Titles and labels with contrasting colors for visibility
plt.title('Total cover versus aspect, with elevation')
plt.xlabel('Aspect (° away from N)')
plt.ylabel('Total moss & lichen cover (%)')

# Set tick and grid colors
plt.tick_params
plt.grid(alpha=0.3, color='gray')
plt.show()

#---------------------------------------------------------
#Separate data into three groups, low, mid and high elevation

# Separate data into three elevation groups
mask_elev_1 = elevation < 1400
mask_elev_2 = (elevation > 1400) & (elevation < 1620)
mask_elev_3 = (elevation > 1620) & (elevation < 1900)

# Plot total cover vs aspect below 1400m
plt.figure(dpi=300)
plt.figure(figsize=(8, 4))
plt.grid(alpha=0.3)
plt.scatter(aspect[mask_elev_1], totcover[mask_elev_1], 20, c='maroon')
plt.title(f'Total cover versus aspect, below 1400m')
plt.xlabel('Aspect (° away from N)')
plt.ylabel('Total moss & lichen cover (%)')
plt.show()


# Plot total cover vs aspect between 1400 and 1620m
plt.figure(dpi=300)
plt.figure(figsize=(8, 4))
plt.grid(alpha=0.3)
plt.scatter(aspect[mask_elev_2], totcover[mask_elev_2], 20, c='maroon')
plt.title(f'Total cover versus aspect, between 1400 and 1620m')
plt.xlabel('Aspect (° away from N)')
plt.ylabel('Total moss & lichen cover (%)')
plt.show()


# Plot total cover vs aspect above 1620m
plt.figure(dpi=300)
plt.figure(figsize=(8, 4))
plt.grid(alpha=0.3)
plt.scatter(aspect[mask_elev_3], totcover[mask_elev_3], 20, c='maroon')
plt.title(f'Total cover versus aspect, above 1620m')
plt.xlabel('Aspect (° away from N)')
plt.ylabel('Total moss & lichen cover (%)')
plt.show()
