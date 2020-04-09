# -*- coding: utf-8 -*-



# Lesson 1: Create Series/DataFrame

from pandas import DataFrame, Series

# 创建Series
se = Series([2, 4, 6, 8], index=['a', 'b', 'c', 'd'])  # 元素、索引均以列表形式给出
print(se)
# a    2
# b    4
# c    6
# d    8
# dtype: int64

# 创建DataFrame
# 方法一（利用dict）
data = {'a':[1, 3, 5], 'b':[2, 4, 6], 'c':[1, 2, 3]}  # list形式
# data = {'a':range(2,6), 'b':range(3,7), 'c':range(4,8)}  # range形式也可
# columns大小可以不一致（名称必须与dict中的一致，否则以columns中的名称为准但元素为NaN），但index大小必须一致
df1 = DataFrame(data, columns=['a', 'b', 'c', 'd'], index=['A', 'B', 'C'])  # 注意columns复数、index单数
#    a  b  c    d
# A  1  2  1  NaN
# B  3  4  2  NaN
# C  5  6  3  NaN
df1 = DataFrame(data, index=['W','X','Y'])
#    a  b  c
# W  1  2  1
# X  3  4  2
# Y  5  6  3
# 方法二（利用numpy）
import numpy as np
df2 = DataFrame(np.arange(0,10).reshape(5,2), columns = ['hh','ww'])
print(df2)
#    hh  ww
# 0   0   1
# 1   2   3
# 2   4   5
# 3   6   7
# 4   8   9




# Lesson 2: Read a tabular data file into pandas

import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 1000)

order1 = pd.read_table('D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\chipotle.tsv.txt')  # DataFrame
# 'pd.read_table()' assumes that the file is tab-separeted and the first row is a header row
print(order1.head())  # DataFrame.head(n=5) Return the first n rows.（加上 header row 总共 n + 1 行） DataFrame.tail() Returns the last n rows.

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code'] # define column names
# header指定第几行作为列名（默认为0，否则设置为None并通过names参数设定列名）
order2 = pd.read_table(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\users.txt', sep='|', header=None, names=user_cols)
print(order2.head())
#    user_id  age gender  occupation zip_code
# 0        1   24      M  technician    85711
# 1        2   53      F       other    94043
# 2        3   23      M      writer    32067
# 3        4   24      M  technician    43537
# 4        5   33      F       other    15213
order2 = pd.read_table(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\users.txt', sep='|', header=2)
print(order2.head())
#    3  23  M         writer  32067
# 0  4  24  M     technician  43537
# 1  5  33  F          other  15213
# 2  6  42  M      executive  98101
# 3  7  57  M  administrator  91344
# 4  8  36  M  administrator  05201




# Lesson 3: Select a pandas series from a DataFrame (Each of those columns is known as a pandas series)

import pandas as pd
pd.set_option('display.width', 1000)

# ufo = pd.read_table(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv',sep=',')
ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')  # 与上行等效
print(type(ufo))  # <class 'pandas.core.frame.DataFrame'>
print(ufo['City'])  # select out the 'City' series （显示first 30 rows and ... and last 30 rows of that series）
print(ufo.City)  # 与上行等效。when a series ia added to a DataFrame, its name automatically becomes an attribute of that DataFrame
# we have to use bracket notation to select a series if the series's name has a space in it（与built-in function冲突的也只能用['']这种方式，如ufo['shape']）
print(ufo['Colors Reported'])
print(type(ufo['City']))  # <class 'pandas.core.series.Series'>

# creat a new series/column
# ufo.Location = ufo.City + ',' + ufo.State # 错误，不能用这种方式
ufo['Location'] = ufo.City + ',' + ufo.State  # 正确，只能用这种方式，新列加在最后
print(ufo.Location)




# Lesson 4: Why do some pandas commands end with parentheses (and other commands don't)
# methods are actions/action-oriented/verbs and attributes are just like descriptions/nouns about who you are

import pandas as pd
pd.set_option('display.width', 1000)

movies = pd.read_csv('D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\imdb_1000.csv')
print(movies.describe())  # show descriptive statistics of all numerical columns （若movies.describe(include='all')，则All columns of the input will be included in the output.）（count数量统计，包含0、不包含空值NaN；std标准差；1/4、1/2、3/4分位数）
#        star_rating    duration
# count   979.000000  979.000000
# mean      7.889785  120.979571
# std       0.336069   26.218010
# min       7.400000   64.000000
# 25%       7.600000  102.000000
# 50%       7.800000  117.000000
# 75%       8.100000  134.000000
# max       9.300000  242.000000
print(movies.shape)
# (979, 6)
print(movies.dtypes)  # 注意加s
# star_rating       float64
# title              object
# content_rating     object
# genre              object
# duration            int64
# actors_list        object
# dtype: object
print(movies.describe(include=['object', 'float64']))  # describe columns with the type 'object' and 'float64'（include里以列表形式传入类型）(unique指独一无二的值的数量；top指出现次数最多的值(the most common value)；fre指top对应的值出现的次数(the most common value's frequency)）
#         star_rating    title content_rating  genre                                             actors_list
# count    979.000000      979            976    979                                                     979
# unique          NaN      975             12     16                                                     969
# top             NaN  Dracula              R  Drama  [u'Daniel Radcliffe', u'Emma Watson', u'Rupert Grint']
# freq            NaN        2            460    278                                                       6
# mean       7.889785      NaN            NaN    NaN                                                     NaN
# std        0.336069      NaN            NaN    NaN                                                     NaN
# min        7.400000      NaN            NaN    NaN                                                     NaN
# 25%        7.600000      NaN            NaN    NaN                                                     NaN
# 50%        7.800000      NaN            NaN    NaN                                                     NaN
# 75%        8.100000      NaN            NaN    NaN                                                     NaN
# max        9.300000      NaN            NaN    NaN                                                     NaN




# Lesson 5: Reanme columns in a pandas DataFrame

import pandas as pd

pd.set_option('display.width', 1000)

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')
print(ufo.columns)  # Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')
print(ufo.columns.tolist())  # ['City', 'Colors Reported', 'Shape Reported', 'State', 'Time']

# 方法一（用rename方法，传入dict，有inplace参数）
# 应该用这种方法（inplace=True 修改原有DataFrame，不生成新的DataFrame）
ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)
print(ufo.columns)  # Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')
print(type(ufo))  # <class 'pandas.core.frame.DataFrame'>

# 有误（说明inplace=True直接修改原有DataFrame，返回None）
ufo1 = ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)
print(ufo1)  # None
print(type(ufo1))  # <class 'NoneType'>

# inplace=False 生成新的DataFrame（inplace默认是'False'）
ufo2 = ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=False)
print(ufo.columns)  # Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')
print(ufo2.columns)  # Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 'Time'], dtype='object')
print(type(ufo2))  # <class 'pandas.core.frame.DataFrame'>


# 方法二（将新名以列表形式赋给ufo.column）
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols
print(ufo.columns)  # Index(['city', 'colors reported', 'shape reported', 'state', 'time'], dtype='object')

# 或 (header=0 means that the 0th row of the underlying? file has exiting column names and i pass it new column names, these will overwrite them)
ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv', names=ufo_cols)
print(ufo.columns)  # Index(['city', 'colors reported', 'shape reported', 'state', 'time'], dtype='object')

# bonus tip: ufo.columns.str.replace
ufo.columns = ufo.columns.str.replace(' ', '-') # 用'-'替换' '
print(ufo.columns)  # Index(['city', 'colors-reported', 'shape-reported', 'state', 'time'], dtype='object')


# https://blog.csdn.net/tanzuozhev/article/details/76645567
print(ufo.columns.values)  # ['City' 'Colors Reported' 'Shape Reported' 'State' 'Time']
print(type(ufo.columns.values))  # <class 'numpy.ndarray'> （不带逗号，不是list）
col_names = ufo.columns.values
col_names[1] = 'color'
ufo.columns = col_names
print(ufo.columns)  # Index(['City', 'color', 'Shape Reported', 'State', 'Time'], dtype='object')
