# -*- coding: utf-8 -*-

# Lesson 21: Make pandas DataFrame smaller and faster

import pandas as pd
pd.set_option('display.width', 1000)

drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')

print(drinks.info())  # info带()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 193 entries, 0 to 192
# Data columns (total 6 columns):
# country                         193 non-null object
# beer_servings                   193 non-null int64
# spirit_servings                 193 non-null int64
# wine_servings                   193 non-null int64
# total_litres_of_pure_alcohol    193 non-null float64
# continent                       193 non-null object
# dtypes: float64(1), int64(3), object(2)
# memory usage: 9.1+ KB
# None
# Why is there a + in 9.1+ kB? Because object columns are reference to other objects,
# pandas wants this info method to run fast so it doesn't actually go out and look at the objects and
# figure out how much space they take. It actually just figures out how much space the references to those
# objects take, so it's saying it's at least 9.1+ kilobytes. But it might be a lot more depending on what's in those
# object columns.
print(drinks.info(memory_usage='deep'))
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 193 entries, 0 to 192
# Data columns (total 6 columns):
# country                         193 non-null object
# beer_servings                   193 non-null int64
# spirit_servings                 193 non-null int64
# wine_servings                   193 non-null int64
# total_litres_of_pure_alcohol    193 non-null float64
# continent                       193 non-null object
# dtypes: float64(1), int64(3), object(2)
# memory usage: 30.4 KB
# None
print(drinks.memory_usage())  # 每一列所占空间，单位是bytes，not kilobytes
# Index                             80
# country                         1544
# beer_servings                   1544
# spirit_servings                 1544
# wine_servings                   1544
# total_litres_of_pure_alcohol    1544
# continent                       1544
# dtype: int64
print(drinks.memory_usage(deep=True))
# Index                              80
# country                         12588
# beer_servings                    1544
# spirit_servings                  1544
# wine_servings                    1544
# total_litres_of_pure_alcohol     1544
# continent                       12332
# dtype: int64
print(drinks.memory_usage(deep=True).sum())  # 31176

# category是用integer代替string，可减小内存（仅限于object column of strings that only has a few different values)
drinks['continent'] = drinks.continent.astype('category')
print(drinks.dtypes)
# country                           object
# beer_servings                      int64
# spirit_servings                    int64
# wine_servings                      int64
# total_litres_of_pure_alcohol     float64
# continent                       category
# dtype: object
print(drinks.continent.head())
# 0      Asia
# 1    Europe
# 2    Africa
# 3    Europe
# 4    Africa
# Name: continent, dtype: category
# Categories (6, object): [Africa, Asia, Europe, North America, Oceania, South America]
print(drinks.continent.cat.codes.head())  # 对应在category中的序号
# 0    1
# 1    2
# 2    0
# 3    2
# 4    0
# dtype: int8
print(drinks.memory_usage(deep=True))  # 减小了continent占用的内存
# Index                              80
# country                         12588
# beer_servings                    1544
# spirit_servings                  1544
# wine_servings                    1544
# total_litres_of_pure_alcohol     1544
# continent                         744
# dtype: int64

# bonus tip
df = pd.DataFrame({'ID':[100, 101, 102, 103], 'quality':['good', 'very good', 'good', 'excellent']})
print(df)
#     ID    quality
# 0  100       good
# 1  101  very good
# 2  102       good
# 3  103  excellent
print(df.sort_values('quality'))  # alphabetical order  区别于print(df.quality.sort_values())输出Series
#     ID    quality
# 3  103  excellent
# 0  100       good
# 2  102       good
# 1  101  very good
df['quality'] = df.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True)
print(df.quality)
# 0         good
# 1    very good
# 2         good
# 3    excellent
# Name: quality, dtype: category
# Categories (3, object): [good < very good < excellent]
print(df.sort_values('quality'))  # 按照自定义的顺序排序
#     ID    quality
# 0  100       good
# 2  102       good
# 1  101  very good
# 3  103  excellent

# use boolean conditions
print(df.loc[df.quality > 'good', :])
#     ID    quality
# 1  101  very good
# 3  103  excellent




# Lesson 22: Use pandas with scikit-learn to create Kaggle submissions

import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns',None)  # 否则中间会显示省略号，还有display.max_rows

train = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\titanic_train.csv')
feature_cols = ['Pclass', 'Parch']
x = train.loc[:, feature_cols]  # feature matrix
y = train.Survived  # response/target factor
# no need to convert them to numpy arrays, scikit-learn will understand
...
# pd.DataFrame({'PassengerID':test.PassengerID, 'Survived':new_pred_class}).set_index('PassengerID').to_csv('sub.csv')

# bonus tip
train.to_pickle('train.pkl')  # 使用DataFrame的to_pickle属性就可以生成pickle文件对数据进行永久储存
pd.read_pickle('train.pkl')  # 使用pandas库的pd.read_pickle读取pickle数据




# Lesson 23: More of your pandas questions answered

import pandas as pd
pd.set_option('display.width', 1000)

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')

# 等效either is fine
print(pd.isnull(ufo).head())  # top-level function
print(ufo.isnull().head())  # method of a DataFrame or a Series

# difference of range index between loc and iloc
print(ufo.loc[0:4])  # 包含尾
#                    City Colors Reported       ...        State             Time
# 0                Ithaca             NaN       ...           NY   6/1/1930 22:00
# 1           Willingboro             NaN       ...           NJ  6/30/1930 20:00
# 2               Holyoke             NaN       ...           CO  2/15/1931 14:00
# 3               Abilene             NaN       ...           KS   6/1/1931 13:00
# 4  New York Worlds Fair             NaN       ...           NY  4/18/1933 19:00
#
# [5 rows x 5 columns]
print(ufo.iloc[0:4])  # 不包含尾 numpy syntax that pandas reuses for iloc
#           City Colors Reported       ...        State             Time
# 0       Ithaca             NaN       ...           NY   6/1/1930 22:00
# 1  Willingboro             NaN       ...           NJ  6/30/1930 20:00
# 2      Holyoke             NaN       ...           CO  2/15/1931 14:00
# 3      Abilene             NaN       ...           KS   6/1/1931 13:00
#
# [4 rows x 5 columns]

# random rows
print(ufo.sample(n=3))  # n可省略
#               City Colors Reported Shape Reported State             Time
# 9457    Sacramento             NaN          LIGHT    CA   6/30/1996 3:00
# 5024  Proctorville            BLUE           DISK    OH   5/5/1984 12:00
# 7821       Seattle             NaN            NaN    WA  2/19/1995 19:00
#
# [3 rows x 5 columns]
print(ufo.sample(n=3, random_state=42))  # 每次运行结果一样
print(ufo.sample(frac=0.75, random_state=99))  # a fraction of rows 每次运行结果一样

# bonus tip: machine learning training data and non-overlapping test data
train = ufo.sample(frac=0.75, random_state=99) # train contains 75% of the rows
test = ufo.loc[~ufo.index.isin(train.index), :] # test contains 25% fo the rows and those 25% are completely exculsive of the training set




# Lesson 24: Create dummy variables（虚拟变量/哑变量） in pandas (用map()，传入dict) (get_dummies是top-level function)

import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns',None)

train = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\titanic_train.csv')
print(train.head())
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
# 4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
train['Sex_Male'] = train.Sex.map({'male':1, 'female':0})
print(train.head())
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked  Sex_Male
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S         1
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C         0
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S         0
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S         0
# 4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S         1
print(pd.get_dummies(train.Sex).head())
#    female  male
# 0       0     1
# 1       1     0
# 2       1     0
# 3       1     0
# 4       0     1
print(pd.get_dummies(train.Sex).iloc[:, 1:].head())
#    male
# 0     1
# 1     0
# 2     0
# 3     0
# 4     1
print(pd.get_dummies(train.Sex, prefix='Sex').head())  # 前面加Sex_
#    Sex_female  Sex_male
# 0           0         1
# 1           1         0
# 2           1         0
# 3           1         0
# 4           0         1
print(train.Embarked.value_counts())
# S    644
# C    168
# Q     77
# Name: Embarked, dtype: int64
print(pd.get_dummies(train.Embarked, prefix='Embarked').head())
#    Embarked_C  Embarked_Q  Embarked_S
# 0           0           0           1
# 1           1           0           0
# 2           0           0           1
# 3           0           0           1
# 4           0           0           1
embarked_dummy = pd.get_dummies(train.Embarked, prefix='Embarked').head()
train = pd.concat([train, embarked_dummy], axis=1)
print(train.head())
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked  Sex_Male  Embarked_C  Embarked_Q  Embarked_S
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S         1         0.0         0.0         1.0
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C         0         1.0         0.0         0.0
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S         0         0.0         0.0         1.0
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S         0         0.0         0.0         1.0
# 4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S         1         0.0         0.0         1.0

# bonus tip
train = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\titanic_train.csv')
print(pd.get_dummies(train, columns=['Sex', 'Embarked']).head())
#    PassengerId  Survived  Pclass                                               Name   Age  SibSp  Parch            Ticket     Fare Cabin  Sex_female  Sex_male  Embarked_C  Embarked_Q  Embarked_S
# 0            1         0       3                            Braund, Mr. Owen Harris  22.0      1      0         A/5 21171   7.2500   NaN           0         1           0           0           1
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  38.0      1      0          PC 17599  71.2833   C85           1         0           1           0           0
# 2            3         1       3                             Heikkinen, Miss. Laina  26.0      0      0  STON/O2. 3101282   7.9250   NaN           1         0           0           0           1
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  35.0      1      0            113803  53.1000  C123           1         0           0           0           1
# 4            5         0       3                           Allen, Mr. William Henry  35.0      0      0            373450   8.0500   NaN           0         1           0           0           1
print(pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True).head())
#    PassengerId  Survived  Pclass                                               Name   Age  SibSp  Parch            Ticket     Fare Cabin  Sex_male  Embarked_Q  Embarked_S
# 0            1         0       3                            Braund, Mr. Owen Harris  22.0      1      0         A/5 21171   7.2500   NaN         1           0           1
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  38.0      1      0          PC 17599  71.2833   C85         0           0           0
# 2            3         1       3                             Heikkinen, Miss. Laina  26.0      0      0  STON/O2. 3101282   7.9250   NaN         0           0           1
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  35.0      1      0            113803  53.1000  C123         0           0           1
# 4            5         0       3                           Allen, Mr. William Henry  35.0      0      0            373450   8.0500   NaN         1           0           1




# Lesson 25: Work with dates and times in pandas (to_datetime是top-level function)
# date string is in different order i.e-  'd/m/y'   or   'y/m/d'  etc. pandas will usually be able to guess the format.
import pandas as pd

ufo = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\ufo.csv')
print(ufo.dtypes)
# City               object
# Colors Reported    object
# Shape Reported     object
# State              object
# Time               object
# dtype: object
print(ufo.Time.str.slice(-5, -3).astype(int).head())  # 字符串操作：从后往前第5到第3之前的一个（两位） str转换为int
# 0    22
# 1    20
# 2    14
# 3    13
# 4    19
# Name: Time, dtype: int32

ufo['Time'] = pd.to_datetime(ufo.Time)  # Time类型转换为datetime64[ns]
print(ufo.dtypes)
# City                       object
# Colors Reported            object
# Shape Reported             object
# State                      object
# Time               datetime64[ns]
# dtype: object
# datetime的作用可以提取时间、日、月、星期等
print(ufo.Time.dt.hour.head())
# 0    22
# 1    20
# 2    14
# 3    13
# 4    19
# Name: Time, dtype: int64
print(ufo.Time.dt.weekday_name.head())
# 0     Sunday
# 1     Monday
# 2     Sunday
# 3     Monday
# 4    Tuesday
# Name: Time, dtype: object
print(ufo.Time.dt.dayofyear.head())  # 一年中的第几天
# 0    152
# 1    181
# 2     46
# 3    152
# 4    108
# Name: Time, dtype: int64

ts = pd.to_datetime('1/1/1999')  # 1999-01-01 00:00:00
print(ufo.loc[ufo.Time >= ts, :].head())  # 可以做数值比较（要通过比较结果筛选，前面用loc[]）
#                     City         ...                        Time
# 12832          Loma Rica         ...         1999-01-01 02:30:00
# 12833            Bauxite         ...         1999-01-01 03:00:00
# 12834           Florence         ...         1999-01-01 14:00:00
# 12835       Lake Henshaw         ...         1999-01-01 15:00:00
# 12836  Wilmington Island         ...         1999-01-01 17:15:00
#
# [5 rows x 5 columns]
print(ufo.Time.max())  # 2000-12-31 23:59:00（latest date)
print(ufo.Time.max() - ufo.Time.min())  # 25781 days 01:59:00
print((ufo.Time.max() - ufo.Time.min()).days)  # 25781

# bonus tip
import matplotlib.pyplot as plt
ufo['Year'] = ufo.Time.dt.year  # 增加一列Year （要先ufo['Time'] = pd.to_datetime(ufo.Time)，才能.dt）
print(ufo.head())
#                    City Colors Reported  ...                 Time  Year
# 0                Ithaca             NaN  ...  1930-06-01 22:00:00  1930
# 1           Willingboro             NaN  ...  1930-06-30 20:00:00  1930
# 2               Holyoke             NaN  ...  1931-02-15 14:00:00  1931
# 3               Abilene             NaN  ...  1931-06-01 13:00:00  1931
# 4  New York Worlds Fair             NaN  ...  1933-04-18 19:00:00  1933
#
# [5 rows x 6 columns]
ufo.Year.value_counts().sort_index().plot()  # 按index排序（日期从小到大）
plt.show()
