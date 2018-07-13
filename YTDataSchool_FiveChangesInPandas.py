# -*- coding: utf-8 -*-




# 1. ix[] has been deprecated

import pandas as pd

drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv', index_col='country')
print(drinks.head())
#              beer_servings    ...      continent
# country                       ...
# Afghanistan              0    ...           Asia
# Albania                 89    ...         Europe
# Algeria                 25    ...         Africa
# Andorra                245    ...         Europe
# Angola                 217    ...         Africa
#
# [5 rows x 5 columns]

# access the element '25'
print(drinks.loc['Algeria', 'beer_servings'])
print(drinks.iloc[2, 0])
print(drinks.ix['Algeria', 0])  # no deprecated-future-warning?
# alternative
print(drinks.loc['Algeria', drinks.columns[0]])
print(drinks.iloc[drinks.index.get_loc('Algeria'), 0])
print(drinks.loc[drinks.index[2], 'beer_servings'])
print(drinks.iloc[2, drinks.columns.get_loc('beer_servings')])




# 2. Aliases have been added for isnull and notnull

import pandas as pd

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')
print(ufo.head())
#                    City Colors Reported       ...        State             Time
# 0                Ithaca             NaN       ...           NY   6/1/1930 22:00
# 1           Willingboro             NaN       ...           NJ  6/30/1930 20:00
# 2               Holyoke             NaN       ...           CO  2/15/1931 14:00
# 3               Abilene             NaN       ...           KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN       ...           NY  4/18/1933 19:00
#
# [5 rows x 5 columns]

print(ufo.isnull().head())
#     City  Colors Reported  Shape Reported  State   Time
# 0  False             True           False  False  False
# 1  False             True           False  False  False
# 2  False             True           False  False  False
# 3  False             True           False  False  False
# 4  False             True           False  False  False
print(ufo.notnull().head())
#    City  Colors Reported  Shape Reported  State  Time
# 0  True            False            True   True  True
# 1  True            False            True   True  True
# 2  True            False            True   True  True
# 3  True            False            True   True  True
# 4  True            False            True   True  True
print(ufo.dropna().head())
#           City Colors Reported       ...        State             Time
# 12      Belton             RED       ...           SC  6/30/1939 20:00
# 19  Bering Sea             RED       ...           AK  4/30/1943 23:00
# 36  Portsmouth             RED       ...           VA   7/10/1945 1:30
# 44   Blairsden           GREEN       ...           CA  6/30/1946 19:00
# 82    San Jose            BLUE       ...           CA  7/15/1947 21:00
#
# [5 rows x 5 columns]
print(ufo.fillna(value='UNKNOWN').head())
#                    City Colors Reported       ...        State             Time
# 0                Ithaca         UNKNOWN       ...           NY   6/1/1930 22:00
# 1           Willingboro         UNKNOWN       ...           NJ  6/30/1930 20:00
# 2               Holyoke         UNKNOWN       ...           CO  2/15/1931 14:00
# 3               Abilene         UNKNOWN       ...           KS   6/1/1931 13:00
# 4  New York Worlds Fair         UNKNOWN       ...           NY  4/18/1933 19:00
#
# [5 rows x 5 columns]

# new alias for isnull
print(ufo.isna().head())
# new alias for notnull
print(ufo.notna().head())




# 3. drop() now accepts 'index' and 'columns' keywords

import pandas as pd

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')
print(ufo.head())
#                    City Colors Reported       ...        State             Time
# 0                Ithaca             NaN       ...           NY   6/1/1930 22:00
# 1           Willingboro             NaN       ...           NJ  6/30/1930 20:00
# 2               Holyoke             NaN       ...           CO  2/15/1931 14:00
# 3               Abilene             NaN       ...           KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN       ...           NY  4/18/1933 19:00
#
# [5 rows x 5 columns]

# old way to drop rows: specify labels and axis
print(ufo.drop([0,1], axis=0).head())
print(ufo.drop([0,1], axis='index').head())
#                    City Colors Reported       ...        State             Time
# 2               Holyoke             NaN       ...           CO  2/15/1931 14:00
# 3               Abilene             NaN       ...           KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN       ...           NY  4/18/1933 19:00
# 5           Valley City             NaN       ...           ND  9/15/1934 15:30
# 6           Crater Lake             NaN       ...           CA   6/15/1935 0:00
#
# [5 rows x 5 columns]

# new way to drop rows: specify index
print(ufo.drop(index=[0,1]).head())


# old way to drop columns: specify labels and axis
print(ufo.drop(['City','State',], axis=1).head())
print(ufo.drop(['City','State',], axis='columns').head())
#   Colors Reported Shape Reported             Time
# 0             NaN       TRIANGLE   6/1/1930 22:00
# 1             NaN          OTHER  6/30/1930 20:00
# 2             NaN           OVAL  2/15/1931 14:00
# 3             NaN           DISK   6/1/1931 13:00
# 4             NaN          LIGHT  4/18/1933 19:00

# new way to drop columns: specify columns
print(ufo.drop(columns=['City','State']).head())




# 4. rename and reindex now accept 'axis' keyword

import pandas as pd

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')

# old way
print(ufo.rename(columns={'City':'CITY', 'State':'STATE'}).head())

# new way
print(ufo.rename({'City':'CITY', 'State':'STATE'}, axis='columns').head())

print(ufo.rename(str.upper, axis='columns').head())  # 所有columns大写
#                    CITY COLORS REPORTED       ...        STATE             TIME
# 0                Ithaca             NaN       ...           NY   6/1/1930 22:00
# 1           Willingboro             NaN       ...           NJ  6/30/1930 20:00
# 2               Holyoke             NaN       ...           CO  2/15/1931 14:00
# 3               Abilene             NaN       ...           KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN       ...           NY  4/18/1933 19:00
#
# [5 rows x 5 columns]




# 5. ordered categories must be specified independent of the data

import pandas as pd

df = pd.DataFrame({'ID':[100, 101, 102, 103],
                   'quality':['good', 'very good', 'good', 'excellent']})
print(df)
#     ID    quality
# 0  100       good
# 1  101  very good
# 2  102       good
# 3  103  excellent

# old way to create an ordered category (deprecated)
# FutureWarning: specifying 'categories' or 'ordered' in .astype() is deprecated; pass a CategoricalDtype instead
print(df.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True))
# 0         good
# 1    very good
# 2         good
# 3    excellent
# Name: quality, dtype: category
# Categories (3, object): [good < very good < excellent]

# new way to create an ordered categor
from pandas.api.types import CategoricalDtype
quality_cat = CategoricalDtype(['good', 'very good', 'excellent'], ordered=True)
df['quality'] = df.quality.astype(quality_cat)
print(df.quality)
# 0         good
# 1    very good
# 2         good
# 3    excellent
# Name: quality, dtype: category
# Categories (3, object): [good < very good < excellent]
