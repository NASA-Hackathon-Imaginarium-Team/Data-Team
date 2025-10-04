import pandas as pd

# Read the Kepler dataset, skipping comment lines
df = pd.read_csv('Kepler Objects of Interest.csv', comment='#')

print(f"Original dataset size: {len(df)} rows")
print(f"koi_disposition value counts:")
print(df['koi_disposition'].value_counts())

# Drop rows where koi_disposition is CANDIDATE
df_filtered = df[df['koi_disposition'] != 'CANDIDATE']
# drop koi_pdisposition column
df_filtered = df_filtered.drop(columns=['koi_pdisposition'])
df_filtered = df_filtered.drop(columns=['kepler_name'])
df_filtered = df_filtered.drop(columns=['kepoi_name'])

print(f"\nFiltered dataset size: {len(df_filtered)} rows")
print(f"Rows removed: {len(df) - len(df_filtered)}")

# Save to CSV
output_file = 'Kepler Objects of Interest - Filtered.csv'
df_filtered.to_csv(output_file, index=False)
print(f"\nFiltered data saved to '{output_file}'")
