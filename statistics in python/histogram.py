import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)
plt.hist(in_bloom,range=(0,365),bins=365)
plt.xlabel('Days')
plt.ylabel('Count')
plt.title('number of flowers blooming each day')
plt.subplot(212)
plt.hist(flights,range=(0,365),bins=365)
plt.xlabel('Days')
plt.ylabel('Count')
plt.title('number of flights per day')
plt.tight_layout()
plt.show()


plt.show()
