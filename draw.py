import matplotlib.pyplot as plt
import pandas


def prime_count(filename):
    return pandas.read_csv(filename)['count'].sum() - 1


def plot_frequency(_pow):
    df1 = pandas.read_csv(f'results/pow_{_pow}.csv')
    df1.plot(x='difference', y='count')

    plt.xlabel('Difference between nearest primes')
    plt.ylabel('Count of differences')
    plt.title(f'Frequency of prime differences (2^{_pow}, 2^{_pow} + 10^7)')

    plt.show()


def plot_frequency_mod_6(_pow):
    df = pandas.read_csv(f'results/pow_{_pow}.csv')
    df1 = df.loc[df['difference'] % 6 == 0]
    ax = df1.plot(x='difference', y='count', label='difference % 6 == 0')
    df2 = df.loc[df['difference'] % 6 != 0]
    df2.plot(x='difference', y='count', label='difference % 6 != 0', ax=ax)

    plt.xlabel('Difference between nearest primes')
    plt.ylabel('Count of differences')
    plt.title(f'Frequency of prime differences mod 6 (2^{_pow}, 2^{_pow} + 10^7)')

    plt.show()


plot_frequency_mod_6(512)
