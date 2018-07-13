# -*- coding: utf-8 -*-




# Lesson 6: Remove columns from a pandas DataFrame

import pandas as pd
pd.set_option('display.width', 1000)

fortune = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\fortune500.csv')

# 删除一列(axis=1)（传入column_name/axis/inplace,，默认axis=0/inplace=False）
fortune.drop('Revenue (in millions)', axis=1, inplace=True)
print(fortune.head())
# 或
del fortune['Profit (in millions)']
print(fortune.head())
# 删除多列（用列表给出）
fortune.drop(['Year', 'Rank'], axis=1, inplace=True)
print(fortune.head())

# 删除行(axis=0) （传入index/axis/inplace）最左侧的0/1/2/3...称为indices/labels
fortune.drop([0, 1], axis=0, inplace=True)  # 默认axis=0，可以省略
# ufo.drop(ufo[ufo['Shape Reported']=='CIRCLE'].index, axis = 0, inplace=True)
print(fortune.head())




# Lesson 7: Sort a pandas DataFrame or a Series

import pandas as pd
pd.set_option('display.width', 1000)

fortune = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\fortune500.csv')
print(fortune.head())

# sort a Series
# f1 = fortune.Company.sort_values(ascending=False)  # 按照'Company'列倒序排列
f1 = fortune['Company'].sort_values(ascending=False)  # 默认升序ascending=True
print(f1.head())  # 输出'Company' Series
print(fortune.head())  # 输出保持原序的整个DataFrame
print(type(fortune.Company.sort_values()))  # <class 'pandas.core.series.Series'>
# YT评论里的解答
f2 = fortune.Company.copy()
print(f2.sort_values().head())

# sort the DataFrame
fortune.sort_values(by='Revenue (in millions)', inplace=True)  # by=可省略
fortune.sort_values(['Company', 'Revenue (in millions)'], inplace=True)  # 先按Company排序，再按Revenue (in millions)排序
print(fortune.head())




# Lesson 8: Filter rows of a pandas DataFrame by column value

import pandas as pd
pd.set_option('display.width', 1000)

fo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\fortune500.csv')

booleans = []
# 将fo['Profit (in millions)']数据由str型转化为float64型。（若无此句，则输出错误TypeError: '>=' not supported between instances of 'str' and 'int'）
fo['Profit (in millions)'] = pd.to_numeric(fo['Profit (in millions)'], errors='coerce')

print(fo[fo['Profit (in millions)'] >= 20000])  # 输出整个DataFrame（bracket notation，也可以用dot notation)

# 或
for prof in fo['Profit (in millions)']:
    if prof >= 20000:
        booleans.append(True)
    else:
        booleans.append(False)

is_prof = pd.Series(booleans)  # 将booleans转换成Series
print(is_prof.head())

print(fo[is_prof])  # 筛选出is_prof中True（即prof >= 20000）对应的行

# OUTPUT
#        Year  Rank      Company  Revenue (in millions)  Profit (in millions)
# 22001  1999     2   Ford Motor               144416.0               22071.0
# 24501  2004     2  Exxon Mobil               213199.0               21510.0
# 25001  2005     2  Exxon Mobil               270772.0               25330.0


# 输出筛选后的DataFrame的某列
print(fo.loc[fo['Profit (in millions)'] >= 20000, 'Year'])  # fo.loc[行，列] （若列名是profit，可fo.profit>=20000）
print(fo[fo['Profit (in millions)'] >= 20000].Year)  # dot notation（与上行等效）
print(fo[fo['Profit (in millions)'] >= 20000]['Year'])  # bracket notation




# Lesson 9: Apply multiple filter criteria to a pandas DataFrame （用& 或 |）

import pandas as pd
pd.set_option('display.width', 1000)

movie = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\imdb_1000.csv')

print(movie[(movie.duration >= 200) & (movie.genre == 'Drama')])  # 不能用and

# Bonus tip
print(movie[(movie.genre == 'Crime') | (movie.genre == 'Drama') | (movie.genre == 'Action')])
# or
print(movie[movie.genre.isin(['Crime', 'Drama', 'Action'])])  # 用isin函数（参数以列表形式给出）




# Lesson 10: Answer questions

# 1. read from csv file only two columns and ignore others（read_csv()里传入usecols参数）
import pandas as pd
pd.set_option('display.width', 1000)
# ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv', usecols=['City', 'Time'])
ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv', usecols=[0, 4])  # 与上行等效
print(ufo.columns)
# Index(['City', 'Time'], dtype='object')

# 2. read from csv file only first n rows（read_csv()里传入nrows参数）
import pandas as pd
pd.set_option('display.width', 1000)
ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv', nrows=3)  # 只读前三行（不包含head）
print(ufo)
#           City  Colors Reported Shape Reported State             Time
# 0       Ithaca              NaN       TRIANGLE    NY   6/1/1930 22:00
# 1  Willingboro              NaN          OTHER    NJ  6/30/1930 20:00
# 2      Holyoke              NaN           OVAL    CO  2/15/1931 14:00

# iteration （说明Series是可迭代对象）
print(ufo.City)
# 0         Ithaca
# 1    Willingboro
# 2        Holyoke
# Name: City, dtype: object
for c in ufo.City:
    print(c)
# Ithaca
# Willingboro
# Holyoke
for index, row in ufo.iterrows():
    print(index, row.City, row.State)
# 0 Ithaca NY
# 1 Willingboro NJ
# 2 Holyoke CO
