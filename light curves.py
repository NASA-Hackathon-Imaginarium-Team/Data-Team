from astroquery.mast import Catalogs
import pandas as pd
import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt


# open the kepler object of interest dataset
df = pd.read_csv('Kepler Objects of Interest.csv', comment='#')

# for the first, get the light curve data for the first star in the dataset
print(df['kepid'][0])
lc_collection = lk.search_lightcurve(f"KIC {df['kepid'][0]}", mission="Kepler", exptime=1800).download()

print(lc_collection)

# yoink time and pdcsap_flux
time = lc_collection.time
flux = lc_collection.pdcsap_flux
# normalize the flux
flux = (flux - flux.mean()) / flux.std()
flux_magnitude = -2.5 * np.log10(flux)
mmag = (flux_magnitude - np.median(flux_magnitude)) * 1000

# period
period = df['koi_period'][0]
# epoch
epoch = df['koi_time0bk'][0]

# phase: (time - epoch)/period MOD 1
phase = ((time - epoch) / period) % 1

# Combine all quarters into a single light curve
lc = lc_collection.stitch()


# mmag on y-axis

plt.figure(figsize=(10, 6))
plt.scatter(phase, flux, s=1)
plt.xlabel("Phase")
plt.ylabel("Normalized Flux")
plt.title(f"Light Curve for KIC {df['kepid'][0]}")
plt.grid()
plt.savefig(f"lightcurve_KIC_{df['kepid'][0]}.png")
plt.show()

# Save to CSV file
output_file = f"lightcurve_KIC_{df['kepid'][0]}.csv"
lc.to_pandas().to_csv(output_file, index=False)
print(f"Combined light curve saved to {output_file}")
