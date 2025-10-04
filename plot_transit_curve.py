import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Kepler dataset, skipping comment lines
df = pd.read_csv('Kepler Objects of Interest.csv', comment='#')

# Remove rows with missing values in the columns we need
df_clean = df[['koi_time0bk', 'koi_insol']].dropna()

# Create the plot
plt.figure(figsize=(12, 8))
plt.scatter(df_clean['koi_time0bk'], df_clean['koi_insol'], alpha=0.5, s=10)
plt.xlabel('Transit Epoch [BKJD]', fontsize=12)
plt.ylabel('Insolation Flux [Earth flux]', fontsize=12)
plt.title('Transit Curve: Transit Epoch vs Insolation Flux', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the plot
plt.savefig('transit_curve.png', dpi=300, bbox_inches='tight')
print(f"Plot saved as 'transit_curve.png'")
print(f"Total data points plotted: {len(df_clean)}")

# Display the plot
plt.show()
