# -*- coding: utf-8 -*-




# Lesson 11: Use the 'axis' parameter in pandas

import pandas as pd
pd.set_option('display.width', 1000)

drink = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')

# 删除column（drop()要传入axis）
print(drink.drop('continent', axis=1).columns)  # does not actually remove the column but just a temporary thing
# Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol'], dtype='object')
# # 下面这种方式就不行（inplace=True/False的关系）
# drink.drop('continent', axis=1)
# print(drink.columns)
# # Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol', 'continent'], dtype='object')

# 删除row（drop()要传入axis）
print(drink.drop(2, axis=0).head())
#              country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol      continent
# 0        Afghanistan              0                0              0                           0.0           Asia
# 1            Albania             89              132             54                           4.9         Europe
# 3            Andorra            245              138            312                          12.4         Europe
# 4             Angola            217               57             45                           5.9         Africa
# 5  Antigua & Barbuda            102              128             45                           4.9  North America

# mean()
print(drink.mean())  # 默认axis=0即move dowm(move across the rows axis) 对行进行操作（从上往下）
print(drink.mean(axis=0))  # 与上行等效
print(drink.mean(axis='index'))  # 与上行等效（注意index是单数）
# beer_servings                   106.160622
# spirit_servings                  80.994819
# wine_servings                    49.450777
# total_litres_of_pure_alcohol      4.717098
# dtype: float64
print(drink.mean(axis=1).head())  # moving along the row axis (not meaningful)
print(drink.mean(axis='columns').head())  # 与上行等效（注意columns是复数）
# 0      0.000
# 1     69.975
# 2      9.925
# 3    176.850
# 4     81.225
# dtype: float64




# Lesson 12: Use string methods in pandas （str.upper()、str.contains()、str.replace()）

print('hello'.upper())  # HELLO

import pandas as pd
pd.set_option('display.width', 1000)

orders = pd.read_table(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\chipotle.tsv')

# print(orders.item_name.upper())  # 错误，输出Error
print(orders.item_name.str.upper())  # 正确，输出大写
print(orders.head())  # 但这里输出仍是原状

print(orders.item_name.str.contains('Chicken'))  # 输出boolean Series  注意contains带s
print(orders[orders.item_name.str.contains('Chicken')])  # 过滤，输出包含'Chicken'的行

# bonus tip 1
print(orders.choice_description.str.replace('[', ''))  # 用''代替'['，返回替换后的Series
print(orders.choice_description.str.replace('[', '').str.replace(']', ''))  # 返回无[]的Series

# bonus tip 2
print(orders.choice_description.str.replace('[\[\]]', ''))  # 正则表达式（要放在bracket里），返回无[和]的Series




# Lesson 13: Change the data type of a pandas Series （astype(dtype)）

import pandas as pd
pd.set_option('display.width', 1000)

drink = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')

print(drink.dtypes)
# country                          object
# beer_servings                     int64
# spirit_servings                   int64
# wine_servings                     int64
# total_litres_of_pure_alcohol    float64
# continent                        object
# dtype: object

# drink.beer_servings.astype(float)  # 改变之后即throw away，实际上并未改变beer_servings的类型
drink.beer_servings = drink.beer_servings.astype('float')  # beer_servings类型变成float64
print(drink.dtypes)
# country                          object
# beer_servings                   float64
# spirit_servings                   int64
# wine_servings                     int64
# total_litres_of_pure_alcohol    float64
# continent                        object
# dtype: object

# define type of each column before actually reading the csv （read_csv()中dtype以dict形式给出）
drink = pd.read_csv('D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv', dtype={'beer_servings':float})  # float也可加''
print(drink.dtypes)
# country                          object
# beer_servings                   float64
# spirit_servings                   int64
# wine_servings                     int64
# total_litres_of_pure_alcohol    float64
# continent                        object
# dtype: object

orders = pd.read_table('D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\chipotle.tsv')
print(orders.head())
#    order_id  quantity                              item_name                                 choice_description item_price
# 0         1         1           Chips and Fresh Tomato Salsa                                                NaN     $2.39
# 1         1         1                                   Izze                                       [Clementine]     $3.39
# 2         1         1                       Nantucket Nectar                                            [Apple]     $3.39
# 3         1         1  Chips and Tomatillo-Green Chili Salsa                                                NaN     $2.39
# 4         2         2                           Chicken Bowl  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98
print(orders.item_price.str.replace('$', '').dtype)  # 虽然去掉了'$'符号，但依然是object（string)
print(orders.item_price.str.replace('$', '').astype(float).dtype)  # 这样才真正转换成float64

# bonus tip
orders = pd.read_table('D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\chipotle.tsv')
print(orders.item_name.str.contains('Chicken'))  # 输出元素是True/False的Series
print(orders.item_name.str.contains('Chicken').astype(int))  # 输出元素是1/0的Series（将boolean转换成0-1）




# Lesson 14: Use a "groupby" in pandas
# When to use? Anytime you want to analyze some pandas series by some category.

import pandas as pd
pd.set_option('display.width', 1000)

drink = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')

print(drink.beer_servings.mean())
# 106.16062176165804
print(drink.groupby('continent').beer_servings.mean())  # 注意不是drink.continent.groupby('beer_servings').mean()
# continent
# Africa            61.471698
# Asia              37.045455
# Europe           193.777778
# North America    145.434783
# Oceania           89.687500
# South America    175.083333
# Name: beer_servings, dtype: float64
print(drink[drink.continent=='Africa'].beer_servings.mean())  # max()/min()
# 61.471698113207545

# agg() allows us to specify multiple aggregation functions at once
print(drink.groupby('continent').beer_servings.agg(['count', 'max', 'min', 'mean'])) # func不带()且加''，以list形式给出
#                count  max  min        mean
# continent
# Africa            53  376    0   61.471698
# Asia              44  247    0   37.045455
# Europe            45  361    0  193.777778
# North America     23  285    1  145.434783
# Oceania           16  306    0   89.687500
# South America     12  333   93  175.083333

# bonus tip
print(drink.groupby('continent').mean())  # calculate the mean across all of the numeric columns
#                beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
# continent
# Africa             61.471698        16.339623      16.264151                      3.007547
# Asia               37.045455        60.840909       9.068182                      2.170455
# Europe            193.777778       132.555556     142.222222                      8.617778
# North America     145.434783       165.739130      24.521739                      5.995652
# Oceania            89.687500        58.437500      35.625000                      3.381250
# South America     175.083333       114.750000      62.416667                      6.308333
import matplotlib.pyplot as plt
plt.figure = drink.groupby('continent').mean().plot(kind='bar')  # plt.figure = 可省略（figure不带()） plot()里传入kind参数（默认折线），bar加''
plt.show()




# Lesson 15: Explore a pandas Series
# DataFrame和Series都可以describe()。数值型和非数值型的describe()输出信息不同。

import pandas as pd
pd.set_option('display.width', 1000)

movies = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\imdb_1000.csv')
print(movies.shape)  # (979, 6)
print(movies.genre.describe())
# count       979  # the count of non-null values in that Series
# unique       16  # the number of unique values in that Series
# top       Drama  # the most common value in that Series
# freq        278  # the frequency of that most common value
# Name: genre, dtype: object
print(movies.genre.value_counts())
# Drama        278
# Comedy       156
# Action       136
# Crime        124
# Biography     77
# Adventure     75
# Animation     62
# Horror        29
# Mystery       16
# Western        9
# Thriller       5
# Sci-Fi         5
# Film-Noir      3
# Family         2
# History        1
# Fantasy        1
# Name: genre, dtype: int64
print(movies.genre.value_counts(normalize=True))  # percentage
print(type(movies.genre.value_counts()))  # <class 'pandas.core.series.Series'>
print(movies.genre.value_counts().head())  # 因此可以用head() method
print(movies.genre.unique())
# ['Crime' 'Action' 'Drama' 'Western' 'Adventure' 'Biography' 'Comedy'
#  'Animation' 'Mystery' 'Horror' 'Film-Noir' 'Sci-Fi' 'History' 'Thriller'
#  'Family' 'Fantasy']
print(movies.genre.nunique())  # the number of unique values in this Series
# 16
print(pd.crosstab(movies.genre, movies.content_rating))  # 交叉表
# content_rating  APPROVED   G  GP  NC-17  NOT RATED  PASSED  PG  PG-13    R  TV-MA  UNRATED  X
# genre
# Action                 3   1   1      0          4       1  11     44   67      0        3  0
# Adventure              3   2   0      0          5       1  21     23   17      0        2  0
# ...

# bonus tip
import matplotlib.pyplot as plt

# 这种方法没有办法对已经绘制好的图案进行后续操作（如添加标题、坐标轴、添加后续图形等）
plt.figure()  # 无本行结果也一样
movies.duration.plot(kind='hist')  # movies.duration.plot.hist() 等效
plt.figure()  # 本行要有
movies.genre.value_counts().plot(kind='bar')  # movies.genre.value_counts().plot.bar() 等效
plt.show()
