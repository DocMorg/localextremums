import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt


if __name__ == '__main__':
    N = 1000000  # length of an array
    T = 4  # diff between indexes of an array
    D = 4  # diff between values of an array
    x = np.random.uniform(low=-1, high=1, size=N)
    x[0] = 1  # starting value
    x = np.cumsum(x)  # using cumsum for faster generating
    index = []  # array for indexes of local extremums
    mins = argrelextrema(x, np.less)[0]  # array of min local extremums
    maxs = argrelextrema(x, np.greater)[0]  # array of max local extremums
    # print('AutoGenerated numpy massive prepared using np.cumsum() \n', x)
    index.append(mins[0])  # zero will be min
    min_elem = mins[0]
    assert index[0] in mins
    for max_elem in maxs:
        # checking the diff in values and in indexes, write if if suites
        if x[max_elem] - x[min_elem] >= D and max_elem - min_elem >= T:
            # check if there's more suitable local minimum
            min_elem = np.argmin(x[min_elem:max_elem])+min_elem
            index[-1] = min_elem
            index.append(max_elem)
            assert index[-1] in maxs
            assert max_elem - min_elem >= T
            assert x[max_elem] - x[min_elem] >= D
            for i in range(min_elem+1, max_elem):
                assert x[min_elem] < x[i] < x[max_elem]
            for min_elem in mins:
                # checking the diff in values and in indexes, write if if suites
                if x[max_elem] - x[min_elem] >= D and min_elem - max_elem >= T:
                    # check if there's more suitable local maximum
                    max_elem = np.argmax(x[max_elem:min_elem]) + max_elem
                    index[-1] = max_elem
                    index.append(min_elem)
                    assert index[-1] in mins
                    assert min_elem - max_elem >= T
                    assert x[max_elem] - x[min_elem] >= D
                    break
    # draw plot
    # print(mins, '\n', maxs)
    print('Index array: \n', index)
    k = 1000  # length of graph by x
    nums = np.arange(k)
    fig, ax = plt.subplots()
    ax.plot(nums[1:], x[:k-1], color='grey', label='graph')
    # put min extremums with blue dots
    ax.scatter(index[0::2], x[index[0::2]], color='blue', marker='o')
    # put max extremums with red dots
    ax.scatter(index[1::2], x[index[1::2]], color='red', marker='o')
    ax.set_title('Numbers and extremums')
    ax.set_ylabel('Values')
    ax.set_xlim(xmin=1, xmax=k)
    ax.grid()
    fig.tight_layout()
    plt.show()
