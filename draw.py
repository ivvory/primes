import numpy as np
import matplotlib.pyplot as plt
import pandas

df1 = pandas.read_csv('output_high.csv')
df2 = pandas.read_csv('output_low.csv')
df3 = pandas.read_csv('output_mid.csv')
df4 = pandas.read_csv('output_high_high.csv')
print(df1)
# df1.hist(column='difference', bins=15)
df2.hist(bins=15)
df3.hist(bins=10)
df1.hist(bins=10)
df4.hist(bins=10)



# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
#
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.7)
#
#
# plt.xlabel('Smarts')
# plt.ylabel('Count')
# plt.title('Distribution of primes in big intervals')
# plt.axis([40, 160, 0, 0.03])
# # plt.grid(True)
plt.show()
