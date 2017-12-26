import matplotlib.pyplot as plt
import pandas


def prime_count(filename):
    return pandas.read_csv(filename)['count'].sum() - 1


_pow = 2048
df1 = pandas.read_csv(f'results/pow_{_pow}.csv')
df1.plot(x='difference', y='count')

plt.xlabel('Difference between nearest primes')
plt.ylabel('Count of differences')
plt.title(f'Frequency of prime differences (2^{_pow}, 2^{_pow} + 10^7)')

plt.show()
