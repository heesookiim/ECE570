import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from CSV files
clip_data = pd.read_csv('clip.csv')
dino_data = pd.read_csv('dino.csv')

# Display the first few rows of each dataframe to understand their structure
clip_data.head(), dino_data.head()


# Data preparation
epochs = clip_data['Unnamed: 0']
clip_wo_imma = clip_data['w/o IMMA']
clip_w_imma = clip_data['w/ IMMA']
dino_wo_imma = dino_data['w/o IMMA']
dino_w_imma = dino_data['w/ IMMA']

# Creating the plots
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Plot for CLIP
axs[0].plot(epochs, clip_wo_imma, label='w/o IMMA', color='green', linestyle='dashed')
axs[0].plot(epochs, clip_w_imma, label='w/ IMMA', color='blue')
axs[0].set_title('Van Gogh')
axs[0].set_xlabel('# of Epochs')
axs[0].set_ylabel('CLIP')
axs[0].legend()

# Plot for DINO
axs[1].plot(epochs, dino_wo_imma, label='w/o IMMA', color='green', linestyle='dashed')
axs[1].plot(epochs, dino_w_imma, label='w/ IMMA', color='blue')
axs[1].set_title('Van Gogh')
axs[1].set_xlabel('# of Epochs')
axs[1].set_ylabel('DINO')
axs[1].legend()

plt.tight_layout()
plt.show()
