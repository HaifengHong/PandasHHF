# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


print(pd.__version__)
# 0.23.1


# 1. Create a datetime column from a DataFrame

# create an example DataFrame
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]], columns=['month', 'day', 'year', 'hour'])
print(df)
#    month  day  year  hour
# 0     12   25  2017    10
# 1      1   15  2018    11

# create a datetime column from the entire DataFrame
print(pd.to_datetime(df))  # rely on the column naming
# 0   2017-12-25 10:00:00
# 1   2018-01-15 11:00:00
# dtype: datetime64[ns]

# create a datertime column from a subset of columns
print(pd.to_datetime(df[['month', 'day', 'year']]))
# 0   2017-12-25
# 1   2018-01-15
# dtype: datetime64[ns]

# overwrite the index
df.index = pd.to_datetime(df[['month', 'year', 'day']])  # 顺序无所谓
print(df)
#             month  day  year  hour
# 2017-12-25     12   25  2017    10
# 2018-01-15      1   15  2018    11




# 2. Create a category column during file reading

# old way to create a category (after file reading)
drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')
drinks['continent'] = drinks.continent.astype('category')

# new way to create a category (during file reading)
drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv', dtype={'continent': 'category'})




# 3. Convert the data type of multiple columns at once

# old way to convert data types (one at once)
drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')
drinks['beer_servings'] = drinks.beer_servings.astype('float')
drinks['spirit_servings'] = drinks.spirit_servings.astype('float')

# new way to convert data types (all at once)
drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')
drinks = drinks.astype({'beer_servings':'float', 'spirit_servings':'float'})




# 4. Apply multiple aggregations on a Series or DataFrame

drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')

print(drinks.groupby('continent').beer_servings.mean())
# continent
# Africa            61.471698
# Asia              37.045455
# Europe           193.777778
# North America    145.434783
# Oceania           89.687500
# South America    175.083333
# Name: beer_servings, dtype: float64


# old way
print(drinks.groupby('continent').beer_servings.agg(['max', 'min', 'mean']))
#                max  min        mean
# continent
# Africa         376    0   61.471698
# Asia           247    0   37.045455
# Europe         361    0  193.777778
# North America  285    1  145.434783
# Oceania        306    0   89.687500
# South America  333   93  175.083333


# new way
# apply the same aggregations to a Series
print(drinks.beer_servings.agg(['max', 'min', 'mean']))
# max     376.000000
# min       0.000000
# mean    106.160622
# Name: beer_servings, dtype: float64

# apply the same aggregations to a DataFrame
print(drinks.agg(['max', 'min', 'mean']))
#           country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol      continent
# max      Zimbabwe     376.000000       438.000000     370.000000                     14.400000  South America
# min   Afghanistan       0.000000         0.000000       0.000000                      0.000000         Africa
# mean          NaN     106.160622        80.994819      49.450777                      4.717098            NaN


# DataFrame describe method  provides similar functionality but is less flexible
print(drinks.describe())
#        beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol
# count     193.000000       193.000000     193.000000                    193.000000
# mean      106.160622        80.994819      49.450777                      4.717098
# std       101.143103        88.284312      79.697598                      3.773298
# min         0.000000         0.000000       0.000000                      0.000000
# 25%        20.000000         4.000000       1.000000                      1.300000
# 50%        76.000000        56.000000       8.000000                      4.200000
# 75%       188.000000       128.000000      59.000000                      7.200000
# max       376.000000       438.000000     370.000000                     14.400000