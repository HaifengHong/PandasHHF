# -*- coding: utf-8 -*-



# Lesson 16: Handle missing values in pandas
# In pandas version 0.21 (released October 2017), 'isna' and 'notna' are added as aliases for 'isnull' and 'notnull'.

import pandas as pd
pd.set_option('display.width', 1000)

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')

print(ufo.isnull().tail())
print(ufo.notnull().tail())

print(ufo.isnull().sum())  # the number of missing values in each of the columns（常用，看有多少数据丢失）
print(pd.Series([True, False, True]).sum())  # 2 True/False视为1/0，求和
print(ufo[ufo.City.isnull()])

print(ufo.shape)  # (18241, 5)
# drop a row if any of its values are missing
print(ufo.dropna(how='any').shape)  # (2486, 5) 默认how='any'因此可省略 inplace=False
print(ufo.shape)  # (18241, 5) 原来的未变（dropna只是temporary）
# drop a row if all of its values are missing
print(ufo.dropna(how='all').shape)  # (18241, 5)
# drop a row if either 'City' or 'Shape Reported' are missing
print(ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape)  # (15576, 5)

# bouns tip（fill missing values)
print(ufo['Shape Reported'].value_counts())  # 不包含NaN
print(ufo['Shape Reported'].value_counts(dropna=False))  # 包含NaN

ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)  # ufo['Shape Reported'] = ufo['Shape Reported'].fillna(value='VARIOUS') 等效
print(ufo['Shape Reported'].value_counts(dropna=False))




# Lesson 17: Know about the pandas index (Part 1) (index 也叫 row labels)

import pandas as pd
pd.set_option('display.width', 1000)

drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')
print(drinks.head())
#        country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
# 0  Afghanistan              0                0              0                           0.0      Asia
# 1      Albania             89              132             54                           4.9    Europe
# ...

print(drinks.index)  # RangeIndex(start=0, stop=193, step=1)
print(drinks.columns)  # Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol', 'continent'], dtype='object')

print(drinks[drinks.continent=='South America'])
print(drinks.loc[23, 'beer_servings'])  # 245 取数，第23行，'beer_servings'列。注意loc[]不是()

drinks.set_index('country', inplace=True)  # 将'country'列设为index
print(drinks.head())
#              beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
# country
# Afghanistan              0                0              0                           0.0      Asia
# Albania                 89              132             54                           4.9    Europe
print(drinks.index)  # Index(['Afghanistan', 'Albania', ..., 'Zimbabwe'], dtype='object', name='country', length=193)
print(drinks.columns)  # Index(['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol', 'continent'], dtype='object')
print(drinks.shape)  # (193, 5)
print(drinks.loc['Brazil', 'beer_servings'])  # 245 这种取数方式更直观

drinks.index.name = None  # 删掉index name即country
print(drinks.head())  # without index name
#              beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
# Afghanistan              0                0              0                           0.0      Asia
# Albania                 89              132             54                           4.9    Europe
# ...
drinks.index.name = 'country'
drinks.reset_index(inplace=True)
print(drinks.head())
#        country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
# 0  Afghanistan              0                0              0                           0.0      Asia
# 1      Albania             89              132             54                           4.9    Europe
# ...

# bonus tip
print(drinks.describe())  # Series
#        beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
# count     193.000000       193.000000     193.000000                    193.000000
# mean      106.160622        80.994819      49.450777                      4.717098
# std       101.143103        88.284312      79.697598                      3.773298
# ...
print(drinks.describe().loc['std', 'beer_servings'])  # 101.1431025393134




# Lesson 18: Know about the pandas index (Part 2)

import pandas as pd
pd.set_option('display.width', 1000)

drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')

drinks.set_index('country', inplace=True)
print(drinks.head())
print(drinks.continent.value_counts())
# Africa           53
# Europe           45
# Asia             44
# North America    23
# Oceania          16
# South America    12
# Name: continent, dtype: int64
print(drinks.continent.value_counts().values)  # [53 45 44 23 16 12]
print(drinks.continent.value_counts()['Africa'])  # 53
print(drinks.continent.value_counts().sort_values())  # 默认升序sort_values(ascending=True))
print(drinks.continent.value_counts().sort_index())  # index按字母/数字排序（默认升序）

people = pd.Series([30000, 8500], index=['Albania', 'Andorra'], name='population')
print(people)
# Albania    30000
# Andorra     8500
# Name: population, dtype: int64
print(drinks.beer_servings * people)
# Afghanistan                   NaN
# Albania                 2670000.0
# Algeria                       NaN
# Andorra                 2082500.0
# Angola                        NaN
# Antigua & Barbuda             NaN
# ...
print(pd.concat([drinks, people], axis=1).head())
#              beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent  population
# Afghanistan              0                0              0                           0.0      Asia         NaN
# Albania                 89              132             54                           4.9    Europe     30000.0
# Algeria                 25                0             14                           0.7    Africa         NaN
# Andorra                245              138            312                          12.4    Europe      8500.0
# Angola                 217               57             45                           5.9    Africa         NaN




# Lesson 19: Select multiple rows and columns from a pandas DataFrame

import pandas as pd
pd.set_option('display.width', 1000)

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')

print(ufo.head(3))  # the first 3 rows


# row selection
print(ufo.loc[0, :])
# City                       Ithaca
# Colors Reported               NaN
# Shape Reported           TRIANGLE
# State                          NY
# Time               6/1/1930 22:00
# Name: 0, dtype: object
print(ufo.loc[[0, 1, 2], :])
print(ufo.loc[0:2, :])  # 包含第2行（区别于list、range）
print(ufo.loc[0:2])  # 等效，但不推荐（explicit is better than implicit）

# loc[]
# column selection
print(ufo.loc[:, 'City'])
print(ufo.loc[:, ['City', 'State']])

print(ufo.loc[0:2, 'City':'State'])  # 注意不是['City':'State']
print(ufo.head(3).drop('Time', axis=1))  # 等效（加axis参数） # del ufo['Time'] (不能用ufo.Time)

print(ufo[ufo.City=='Oakland'])
print(ufo.loc[ufo.City=='Oakland', :])  # 等效

print(ufo.loc[ufo.City=='Oakland', 'State'])
print(ufo[ufo.City=='Oakland'].State)  # 等效

# iloc[] filters rows and selects columns by integer position
print(ufo.iloc[:, [0,3]])
print(ufo.iloc[:, 0:4])  # 不包含第4列

print(ufo[0:2])  # 第0、1行 （不推荐这种写法，不explicit）

# ix[] allows to mix labels and integers when doing selection（blend between loc and iloc)（has officially been deprecated)
drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')
print(drinks.head())
# print(drinks.ix['Albania', 0])  # Error
print(drinks.ix[1, 'beer_servings'])  # 89
print(drinks.ix['Albania':'Andorra', 0:2])
print(drinks.ix[0:2, 0:2]) # labels三行，columns两列（quite confusing，so不建议用ix）
#        country  beer_servings
# 0  Afghanistan              0
# 1      Albania             89
# 2      Algeria             25




# Lesson 20: Use the "inplace" parameter in pandas

import pandas as pd
pd.set_option('display.width', 1000)

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')

print(ufo.columns)  # Index(['City', 'Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')
print(ufo.drop('City', axis=1).columns)  # Index(['Colors Reported', 'Shape Reported', 'State', 'Time'], dtype='object')

ufo.set_index('Time', inplace=True)  # ufo = ufo.set_index('Time') 等效
print(ufo)
