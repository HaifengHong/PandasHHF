# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# 1 Object Creation


# create a Series
s = pd.Series([1, 3.4, np.nan, np.arange(3)])  # 元素要以列表形式给出
print(s)
# 0            1
# 1          3.4
# 2          NaN
# 3    [0, 1, 2]
# dtype: object


# create a DataFrame
dates = pd.date_range('20130101', periods=6)  # 默认freq='D'（'D'以天为间隔，'T'以分钟，'S'以秒，'M'以月，'3M'以3个月）
#  pd.date_range(start='2018-04-24', end='2018-04-27', periods=3)  # 生成24/25/27, freq=None
print(dates)
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))  # 比columns=['A', 'B', 'C', 'D']写法更简洁
print(df)

df2 = pd.DataFrame({ 'A': 1.,
                     'B': pd.Timestamp('20130102'),
                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D': np.array([3] * 4,dtype='int32'),
                     'E': pd.Categorical(["test","train","test","train"]),
                     'F': 'foo' })
print(df2)
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo




# 2 Viewing Data


print(df.head())
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.values)  # the underlying NumPy data 每一行以list给出
# [[ 1.81774205 -0.99729334  1.21593966  0.15197905]
#  [ 1.85439605 -0.22660996  1.89802889 -0.17302373]
#  [ 0.81865798  0.24635964  2.56841159 -0.51754109]
#  [ 0.56292483 -2.64281725 -0.86864759 -0.132217  ]
#  [ 0.64704487  1.24628227 -0.61727745 -0.35989526]
#  [-0.68344598 -1.89266969  0.28997575 -0.62927136]]
print(df.describe())  # a quick statistic summary of your data
#               A         B         C         D
# count  6.000000  6.000000  6.000000  6.000000
# mean  -0.868647  0.493136 -0.007901 -0.527119
# std    0.928321  0.939735  1.060408  1.491762
# min   -2.035525 -0.544369 -1.105543 -3.034203
# 25%   -1.421475 -0.068466 -0.905028 -1.041131
# 50%   -0.965846  0.230670 -0.096883 -0.408042
# 75%   -0.406549  0.957008  0.732101  0.622710
# max    0.548804  2.010902  1.417885  0.973439
print(df.T)  # Transposing your data
#    2013-01-01  2013-01-02     ...      2013-01-05  2013-01-06
# A    1.096951   -1.150710     ...        0.654937   -0.283626
# B   -0.993457   -0.214703     ...        0.187281   -1.031164
# C    0.321226    0.457932     ...       -2.977882    1.973820
# D    1.103688   -1.241242     ...       -0.264165    1.058030
#
# [4 rows x 6 columns]
print(df.sort_index(ascending=False))  # 默认axis=0, inplace=False
#                    A         B         C         D
# 2013-01-06  0.764681  0.814756 -1.586755 -0.159105
# 2013-01-05  2.265473  0.862731 -0.103365  1.614840
# 2013-01-04 -2.544316 -0.877202 -0.382783  2.144286
# 2013-01-03 -1.094658 -0.613332  0.532245 -1.490205
# 2013-01-02 -0.492868  1.753566  0.670638  0.258518
# 2013-01-01 -0.095917  1.209922  0.334694 -0.231184
print(df.sort_index(axis=1, ascending=False))  # Sorting by an axis 默认ascending=True升序
#                    D         C         B         A
# 2013-01-01  0.736898  0.079144 -0.970967  0.848613
# 2013-01-02 -1.366322  0.645540  1.109221 -1.702136
# 2013-01-03 -1.322482 -1.988157  0.042463  0.304632
# 2013-01-04  0.666114  0.273446 -1.016108 -1.405244
# 2013-01-05 -0.216343  2.869178  0.750119  0.128011
# 2013-01-06  0.869156  0.598721 -1.031959 -1.366274
print(df.sort_values(by='B'))  # Sorting by values B列（默认升序）




# 3 Selection

# Getting
print(df['A'])  # 选列 Selecting a single column, which yields a Series, equivalent to df.A
print(df[['A']])  # 选列 Selecting a single column, which yields a DataFrame
print(df[['A', 'C']])  # 选列 用[]
print(df[:1])  # 选行 Selecting via [], which slices the rows.
#                    A         B         C         D
# 2013-01-01  1.879192 -0.528925 -0.273056  1.283601

# Selection by Label（loc[]生成Series）
# print(df.loc[['2013-01-02','2013-01-04'],:])  # 不明白 KeyError: "None of [['2013-01-02', '2013-01-04']] are in the [index]"
print(df.loc[dates[0]])  # getting a cross section using a label 区别于print(df[:1])（df[:1] slices the rows, 而df.loc[]生成Series）
# A    1.879192
# B   -0.528925
# C   -0.273056
# D    1.283601
# Name: 2013-01-01 00:00:00, dtype: float64
print(df.loc[:,['A','B']])  # Selecting on a multi-axis by label
print(df.loc['20130102':'20130104',['A','B']])  # '20130102':'20130104'不加[]
print(df.loc['20130102',['A','B']])
# A    0.776980
# B    0.816093
# Name: 2013-01-02 00:00:00, dtype: float64
print(df.loc[dates[0],'A'])  # getting a scalar value 单元素就不用[]
print(df.at[dates[0],'A'])  # 与上行等效（at的使用方法与loc类似，但是比loc有更快的访问数据的速度，而且只能访问单个元素，不能访问多个元素。）

# Selection by Position（生成Series）
print(df.iloc[3])  # Select via the position of the passed integers
print(df.iloc[3:5,0:2])  # By integer slices, acting similar to numpy/python （使用:则行列不需加[]）
print(df.iloc[[1,2,4],[0,2]])  # By lists of integer position locations, similar to the numpy/python style（列出详细元素则行列需加[]）
print(df.iloc[1:3,:])  # Slicing rows explicitly
print(df.iloc[:,1:3])  # Slicing columns explicitly
print(df.iloc[1,1])  # Getting a value explicitly
print(df.iat[1,1])  # 与上行等效Getting fast access to a scalar

# Boolean Indexing
print(df.A > 0)  # 生成boolean Series
# 2013-01-01     True
# 2013-01-02    False
# 2013-01-03    False
# 2013-01-04    False
# 2013-01-05    False
# 2013-01-06     True
# Freq: D, Name: A, dtype: bool
print(df[df.A > 0])  # Using a single column's values to select data
#                    A         B         C         D
# 2013-01-01  0.210211  0.205123  0.420011 -0.605540
# 2013-01-06  0.498802  0.259746  0.654506  0.625518
print(df[df > 0])  # Selecting values from a DataFrame where a boolean condition is met
#                    A         B         C         D
# 2013-01-01       NaN  0.666675  0.161066  0.387802
# 2013-01-02  0.958784  0.192638  0.308731       NaN
# 2013-01-03       NaN       NaN       NaN  0.053776
# 2013-01-04  0.171848       NaN  0.873722  1.812336
# 2013-01-05  1.630569       NaN       NaN       NaN
# 2013-01-06       NaN  1.032952       NaN  0.121108
# Using the isin() method for filtering
df3 = df.copy()
df3['E'] = ['one', 'one','two','three','four','three']
#                    A         B         C         D      E
# 2013-01-01 -1.054001  1.574561  1.502924 -0.704023    one
# 2013-01-02  0.022914 -0.429638 -0.712063 -2.177634    one
# 2013-01-03  0.563001 -0.458569  1.252273 -1.141820    two
# 2013-01-04 -0.531754  0.325335  0.073644 -1.107728  three
# 2013-01-05 -1.063415 -0.386210 -0.465371 -1.786887   four
# 2013-01-06 -0.081098 -0.135803 -0.237078 -1.890792  three
print(df3[df3['E'].isin(['two','four'])])  # df3[df3.E.isin(['two','four'])]等效
#                    A         B         C         D     E
# 2013-01-03  0.563001 -0.458569  1.252273 -1.141820   two
# 2013-01-05 -1.063415 -0.386210 -0.465371 -1.786887  four

# Setting
# Setting a new column automatically aligns the data by the indexes
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
df['F'] = s1
df.at[dates[0],'A'] = 0  # Setting values by label
df.iat[0,1] = 0  # Setting values by position
df.loc[:,'D'] = np.array([5] * len(df))  # Setting by assigning with a NumPy array
print(df)
#                    A         B         C  D    F
# 2013-01-01  0.000000  0.000000  0.415011  5  NaN
# 2013-01-02  0.061891  1.768064 -1.036807  5  1.0
# 2013-01-03 -0.242554 -1.051701  1.293475  5  2.0
# 2013-01-04 -1.069789  0.916634  1.807129  5  3.0
# 2013-01-05 -0.539271  1.737878  1.210983  5  4.0
# 2013-01-06 -0.025909  0.040835 -2.126612  5  5.0
df4 = df.copy()
df4[df4 > 0] = -df4  # A where operation with setting




# 4 Missing Data


# Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data
df5 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])  # columns以list形式给出
df5.loc[dates[0]:dates[1],'E'] = 1
print(df5)
print(df5.dropna(how='any'))  # To drop any rows that have missing data.
print(df5.fillna(value=5))  # Filling missing data.
print(pd.isna(df5))  # To get the boolean mask where values are nan.（虽然已用5填充，但仍属于nan，可能是因为inplace=False，原DataFrame未变）




# 5 Operations
# Operations in general exclude missing data.

# Stats
print(df.mean())  # Performing a descriptive statistic 不包含NaN
# A   -0.110416
# B    0.548187
# C    0.429098
# D    0.218791
# dtype: float64
print(df.mean(1))  # Same operation on the other axis
# 2013-01-01   -1.168430
# 2013-01-02    0.355400
# 2013-01-03    0.883531
# 2013-01-04    1.235038
# 2013-01-05    0.649363
# 2013-01-06   -0.326413
# Freq: D, dtype: float64

# Apply
print(df.apply(np.cumsum))  # 沿着row方向（从上往下）累加
print(df.apply(lambda x: x.max() - x.min()))

# Histogramming
s2 = pd.Series(np.random.randint(0, 7, size=10))
print(s2.value_counts())
# 6    5
# 0    2
# 5    1
# 4    1
# 1    1
# dtype: int64

# String Methods
s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s3.str.lower())




# 6 Merge


# Concat
df6 = pd.DataFrame(np.random.randn(5, 4))
#           0         1         2         3
# 0 -1.078443  1.005519 -1.281237  0.843688
# 1  0.818437  1.607356 -0.140013 -0.377372
# 2 -1.000181  1.847057  0.333092 -0.904176
# 3 -0.878796  2.762767  1.511159  0.175878
# 4  0.041001  0.917143 -0.974650 -0.047792
pieces = [df6[:3], df6[3:]]
# [          0         1         2         3
# 0 -1.078443  1.005519 -1.281237  0.843688
# 1  0.818437  1.607356 -0.140013 -0.377372,           0         1         2         3
# 2 -1.000181  1.847057  0.333092 -0.904176
# 3 -0.878796  2.762767  1.511159  0.175878
# 4  0.041001  0.917143 -0.974650 -0.047792]
print(pd.concat(pieces))  # concat()传入list
#           0         1         2         3
# 0 -1.078443  1.005519 -1.281237  0.843688
# 1  0.818437  1.607356 -0.140013 -0.377372
# 2 -1.000181  1.847057  0.333092 -0.904176
# 3 -0.878796  2.762767  1.511159  0.175878
# 4  0.041001  0.917143 -0.974650 -0.047792

# Join
# example 1
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(pd.merge(left, right, on='key'))
#    key  lval  rval
# 0  foo     1     4
# 1  foo     1     5
# 2  foo     2     4
# 3  foo     2     5
# example 2
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(pd.merge(left, right, on='key'))
#    key  lval  rval
# 0  foo     1     4
# 1  bar     2     5

# Append
df7 = pd.DataFrame(np.random.randn(4, 3), columns=['A','B','C'])
s4 = df7.iloc[2]
print(df7.append(s4, ignore_index=True))  # 新行index按顺序往下编。df7并未改变
#           A         B         C
# 0 -0.009674  0.469766  1.211444
# 1 -0.188221  1.212227 -0.177459
# 2 -0.223693  0.157304  0.478856
# 3 -1.076484  0.655263 -0.961934
# 4 -0.223693  0.157304  0.478856
print(df7.append(s4))  # 新行还是原index
#           A         B         C
# 0 -0.009674  0.469766  1.211444
# 1 -0.188221  1.212227 -0.177459
# 2 -0.223693  0.157304  0.478856
# 3 -1.076484  0.655263 -0.961934
# 2 -0.223693  0.157304  0.478856




# 7 Grouping


df8 = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})
print(df8.groupby('A').sum())  # groupby是DataFrame的函数，不是pd
#             C         D
# A
# bar  0.505886 -1.876635
# foo  4.333131 -0.160911
print(df8.groupby(['A','B']).sum())
#                   C         D
# A   B
# bar one   -0.826279 -0.623750
#     three -0.287023 -0.934656
#     two   -0.799268  0.543823
# foo one    0.671641 -0.077534
#     three -0.707932 -0.630983
#     two   -2.529067 -1.364490




# 8 Reshaping


# Stack
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                 ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
print(tuples)
# [('bar', 'one'), ('bar', 'two'), ('baz', 'one'), ('baz', 'two'), ('foo', 'one'), ('foo', 'two'), ('qux', 'one'), ('qux', 'two')]
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
print(df2)
#                      A         B
# first second
# bar   one    -1.071952 -0.779305
#       two     0.312376  1.092419
# baz   one    -0.672488 -1.301370
#       two     0.734665  1.467257

stacked = df2.stack()  # The stack() method "compresses" a level in the DataFrame's columns.
print(stacked)
# bar    one     A   -0.090085
#                B    0.641121
#        two     A   -0.069353
#                B   -0.668279
# baz    one     A   -1.666011
#                B    0.604002
#        two     A    1.064439
#                B   -1.832184
# dtype: float64

# Pivot Tables 数据透视表
df = pd.DataFrame({ 'A': ['one', 'one', 'two', 'three'] * 3,
                    'B': ['A', 'B', 'C'] * 4,
                    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                    'D': np.random.randn(12),
                    'E': np.random.randn(12)})
print(df)
#         A  B    C         D         E
# 0     one  A  foo -0.090795 -0.031392
# 1     one  B  foo  0.670661 -0.473564
# 2     two  C  foo -0.294397 -0.938500
# 3   three  A  bar  1.142138 -1.760756
# 4     one  B  bar -0.464242 -0.747847
# 5     one  C  bar  0.320074 -0.353668
# 6     two  A  foo -0.631601 -2.081452
# 7   three  B  foo -0.223351 -0.334236
# 8     one  C  foo -0.445821 -1.275973
# 9     one  A  bar  0.878320 -0.133317
# 10    two  B  bar -2.368427 -0.981376
# 11  three  C  bar -1.036963 -0.756109
print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))
# C             bar       foo
# A     B
# one   A  0.878320 -0.090795
#       B -0.464242  0.670661
#       C  0.320074 -0.445821
# three A  1.142138       NaN
#       B       NaN -0.223351
#       C -1.036963       NaN
# two   A       NaN -0.631601
#       B -2.368427       NaN
#       C       NaN -0.294397




# Time Series
rng = pd.date_range('1/1/2000', periods=9, freq='T')
# DatetimeIndex(['2000-01-01 00:00:00', '2000-01-01 00:01:00',
#                '2000-01-01 00:02:00', '2000-01-01 00:03:00',
#                '2000-01-01 00:04:00', '2000-01-01 00:05:00',
#                '2000-01-01 00:06:00', '2000-01-01 00:07:00',
#                '2000-01-01 00:08:00'],
#               dtype='datetime64[ns]', freq='T')
ts = pd.Series(range(9), index=rng)
# 2000-01-01 00:00:00    0
# 2000-01-01 00:01:00    1
# 2000-01-01 00:02:00    2
# 2000-01-01 00:03:00    3
# 2000-01-01 00:04:00    4
# 2000-01-01 00:05:00    5
# 2000-01-01 00:06:00    6
# 2000-01-01 00:07:00    7
# 2000-01-01 00:08:00    8
# Freq: T, dtype: int64
print(ts.resample('3T').sum())  # 降低采样频率为三分钟
# 2000-01-01 00:00:00     3
# 2000-01-01 00:03:00    12
# 2000-01-01 00:06:00    21
# Freq: 3T, dtype: int64




# 9 Categoricals

# Convert the raw grades to a categorical data type.
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")  # 增加一列
print(df["grade"])
# 0    a
# 1    b
# 2    b
# 3    a
# 4    a
# 5    e
# Name: grade, dtype: category
# Categories (3, object): [a, b, e]

# Rename the categories to more meaningful names (assigning to Series.cat.categories is inplace!).
df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df)
#    id raw_grade      grade
# 0   1         a  very good
# 1   2         b       good
# 2   3         b       good
# 3   4         a  very good
# 4   5         a  very good
# 5   6         e   very bad

# Reorder the categories and simultaneously add the missing categories (methods under Series .cat return a new Series by default).
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df["grade"])
# 0    very good
# 1         good
# 2         good
# 3    very good
# 4    very good
# 5     very bad
# Name: grade, dtype: category
# Categories (5, object): [very bad, bad, medium, good, very good]

# Sorting is per order in the categories, not lexical order.
print(df.sort_values(by="grade"))
#    id raw_grade      grade
# 5   6         e   very bad
# 1   2         b       good
# 2   3         b       good
# 0   1         a  very good
# 3   4         a  very good
# 4   5         a  very good

# Grouping by a categorical column also shows empty categories.
print(df.groupby("grade").size())  # size带()
# grade
# very bad     1
# bad          0
# medium       0
# good         2
# very good    3
# dtype: int64




# 10 Plotting（下面这种方式可以同时独立显示两张图）

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
# plt.show() 若要先关闭第一个图再显示第二个图，则加上这一行

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
# plt.figure()  # 会出现空白的一张图
df.plot()
plt.legend(loc='best')
plt.show()





# 11 Getting Data In/Out


# CSV
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df.to_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\foo.csv')

# Excel
# Writing to an excel file.
# 要先安装'openpyxl'库，否则ModuleNotFoundError: No module named 'openpyxl'
df.to_excel(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\foo.xlsx', sheet_name='表格1')
# Reading from an excel file.
# 要先安装'xlrd'库，否则ModuleNotFoundError: No module named 'xlrd' # 不加index_col=None, na_values=['NA']也无影响
print(pd.read_excel(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\foo.xlsx', '表格1', index_col=None, na_values=['NA']))
