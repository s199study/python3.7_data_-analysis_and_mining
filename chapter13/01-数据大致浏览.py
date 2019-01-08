import pandas as pd
import numpy as np


if __name__ == '__main__':
    file_name = './data/data1.csv'
    data = pd.read_csv(file_name)
    print(data.head())
    r = [data.min(), data.max(), data.mean(), data.std()]
    r = pd.DataFrame(r, index=['Min', 'Max', 'Mean', 'Std']).T
    r = np.round(r, decimals=2)
    print(r)
    """
            Min         Max        Mean         Std
    x1   3831732.00  7599295.00  5579519.95  1262194.72
    x2       181.54     2110.78      765.04      595.70
    x3       448.19     6882.85     2370.83     1919.17
    x4      7571.00    42049.14    19644.69    10203.02
    x5      6212.70    33156.83    15870.95     8199.77
    x6   6370241.00  8323096.00  7350513.60   621341.85
    x7       525.71     4454.55     1712.24     1184.71
    x8       985.31    15420.14     5705.80     4478.40
    x9        60.62      228.46      129.49       50.51
    x10       65.66      852.56      340.22      251.58
    x11       97.50      120.00      103.31        5.51
    x12        1.03        1.91        1.42        0.25
    x13     5321.00    41972.00    17273.80    11109.19
    y         64.87     2088.14      618.08      609.25
    """

    # Perarson 相关系数
    corr_data = data.corr(method='pearson', min_periods=2)
    corr_data = np.round(corr_data, decimals=2)
    print(corr_data)
    """
           x1    x2    x3    x4    x5    x6    x7    x8    x9   x10   x11   x12   x13     y
    x1   1.00  0.95  0.95  0.97  0.97  0.99  0.95  0.97  0.98  0.98 -0.29  0.94  0.96  0.94
    x2   0.95  1.00  1.00  0.99  0.99  0.92  0.99  0.99  0.98  0.98 -0.13  0.89  1.00  0.98
    x3   0.95  1.00  1.00  0.99  0.99  0.92  1.00  0.99  0.98  0.99 -0.15  0.89  1.00  0.99
    x4   0.97  0.99  0.99  1.00  1.00  0.95  0.99  1.00  0.99  1.00 -0.19  0.91  1.00  0.99
    x5   0.97  0.99  0.99  1.00  1.00  0.95  0.99  1.00  0.99  1.00 -0.18  0.90  0.99  0.99
    x6   0.99  0.92  0.92  0.95  0.95  1.00  0.93  0.95  0.97  0.96 -0.34  0.95  0.94  0.91
    x7   0.95  0.99  1.00  0.99  0.99  0.93  1.00  0.99  0.98  0.99 -0.15  0.89  1.00  0.99
    x8   0.97  0.99  0.99  1.00  1.00  0.95  0.99  1.00  0.99  1.00 -0.15  0.90  1.00  0.99
    x9   0.98  0.98  0.98  0.99  0.99  0.97  0.98  0.99  1.00  0.99 -0.23  0.91  0.99  0.98
    x10  0.98  0.98  0.99  1.00  1.00  0.96  0.99  1.00  0.99  1.00 -0.17  0.90  0.99  0.99
    x11 -0.29 -0.13 -0.15 -0.19 -0.18 -0.34 -0.15 -0.15 -0.23 -0.17  1.00 -0.43 -0.16 -0.12
    x12  0.94  0.89  0.89  0.91  0.90  0.95  0.89  0.90  0.91  0.90 -0.43  1.00  0.90  0.87
    x13  0.96  1.00  1.00  1.00  0.99  0.94  1.00  1.00  0.99  0.99 -0.16  0.90  1.00  0.99
    y    0.94  0.98  0.99  0.99  0.99  0.91  0.99  0.99  0.98  0.99 -0.12  0.87  0.99  1.00
    """
