import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ecdf(data):
    '''
    function to calcuate Empirical Cumulative Distribution Function ECDF
    '''
    # number of points in data
    n = len(data)
    # x-data for ECDF
    x = np.sort(data)
    # y-data for ECDF
    y = np.arange(1, n + 1) / n

    return x, y


def plot_ecdf(data, xlabel_: str, display_percentile: bool=False, percentiles=None):
    '''
    a function to plot ECDF graph. If TRUE, the plot can show defined percentile points
        in RED. Percentiles points should be passed as list.
    '''
    #TODO add a feature to plot multiple features at once

    x, y = ecdf(data) # calculate ECDF before ploting

    # ploting ECDF
    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.xlabel(xlabel_)
    _ = plt.ylabel('ECDF')

    if display_percentile:
        percentiles = np.array(percentiles)
        ptiles_x = np.percentile(x, q=percentiles)
        _ = plt.plot(ptiles_x, percentiles/100, marker='D', color='red', linestyle='none')

    plt.show()


def plot_box_plot(x: str, y: str, data):
    '''
    function to plot box and whiskers plot. x and y should be passed as string and 
        data should be passed as dataframe
    '''
    _ = sns.boxplot(x, y, data=data)
    _ = plt.xlabel(x)
    _ = plt.ylabel(y)
    plt.show()


def plot_scatter_plot(x, y, x_label, y_label, add_lr):
    """    function to display scatter plot of x and y. Function can accept boolean argument to 
    plot linear regression line
    
    Args:
        x (np.array): x data array
        y (np.array): y data array
        x_label (str): x axis label
        y_label (str)): y axis label
        add_lr (bool): indicate if you need to plot linear regression line 
    """
    _ = plt.plot(x, y, marker='.', linestyle='none')
    if add_lr:
        # calculating linear regression
        a, b = np.polyfit(x, y, deg=1)

        #preparing to plot linear regression line
        x_lr = np.array([np.min(x), np.max(x)])
        y_lr = a * x_lr + b

        # ploting linear regression line
        _ = plt.plot(x_lr, y_lr)

    _ = plt.xlabel(x_label)
    _ = plt.ylabel(y_label)
    plt.margins(0.02)
    plt.show()


def find_optimal_parameters(param):
    """Visualize and find the optimal parameter for a linear regression model.
    
    Args:
        param ([type]): [description]
    """

    pass


def compute_pearson_correlation(param):
    pass
    

def generate_bootstrap_replicates(data, func, size=1):

    def bootstarp_replicate_1d(data, func):

        return func(np.random.choice(data, size=len(data)))

    return np.array([bootstarp_replicate_1d(data, func) for _ in range(size)])


def generate_bootstarp_pairs_linreg(x, y, size=1):

    inds = np.arange(len(x))

    bs_slope_replicates = np.empty(size)
    bs_intercept_replicates = np.empty(size)

    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_replicates[i], bs_intercept_replicates[i] = np.polyfit(bs_x, bs_y, deg=1)
    
    return bs_slope_replicates, bs_intercept_replicates



iris = sns.load_dataset('iris')
iris = iris[iris['species'] == 'virginica']
print(iris.tail())

# plot_box_plot('species', 'petal_length', data=iris)
percentiles = [25, 50, 75]
# plot_ecdf(iris['petal_length'], xlabel_='Petal Length', display_percentile=True, percentiles=percentiles)
plot_scatter_plot(x=iris['petal_length'], y=iris['petal_width'], 
                    x_label='petal length', y_label='petal width',
                    add_lr=True)

