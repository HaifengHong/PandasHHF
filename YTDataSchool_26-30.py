# -*- coding: utf-8 -*-

# Lesson 26: Find and remove duplicate rows in pandas
import pandas as pd

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\users.txt', sep='|', header=None, names=user_cols, index_col='user_id')

print(users.shape)  # (943, 4)
print(users.head())
#          age gender  occupation zip_code
# user_id
# 1         24      M  technician    85711
# 2         53      F       other    94043
# 3         23      M      writer    32067
# 4         24      M  technician    43537
# 5         33      F       other    15213
print(users.zip_code.duplicated().sum())  # 148(duplicated()返回True/False)
print(users.duplicated().sum())  # 7
print(users.loc[users.duplicated(), :])
#          age gender occupation zip_code
# user_id
# 496       21      F    student    55414
# 572       51      M   educator    20003
# 621       17      M    student    60402
# 684       28      M    student    55414
# 733       44      F      other    60630
# 805       27      F      other    20009
# 890       32      M    student    97301
print(users.loc[users.duplicated(keep='first'), :])
#          age gender occupation zip_code
# user_id
# 496       21      F    student    55414
# 572       51      M   educator    20003
# 621       17      M    student    60402
# 684       28      M    student    55414
# 733       44      F      other    60630
# 805       27      F      other    20009
# 890       32      M    student    97301
print(users.loc[users.duplicated(keep='last'), :])
#          age gender occupation zip_code
# user_id
# 67        17      M    student    60402
# 85        51      M   educator    20003
# 198       21      F    student    55414
# 350       32      M    student    97301
# 428       28      M    student    55414
# 437       27      F      other    20009
# 460       44      F      other    60630
print(users.loc[users.duplicated(keep=False), :])  # show all duplicated rows
#          age gender occupation zip_code
# user_id
# 67        17      M    student    60402
# 85        51      M   educator    20003
# 198       21      F    student    55414
# 350       32      M    student    97301
# 428       28      M    student    55414
# 437       27      F      other    20009
# 460       44      F      other    60630
# 496       21      F    student    55414
# 572       51      M   educator    20003
# 621       17      M    student    60402
# 684       28      M    student    55414
# 733       44      F      other    60630
# 805       27      F      other    20009
# 890       32      M    student    97301
print(users.drop_duplicates(keep='first').shape)  # (936, 4) keep=first/'last/False (not inplace)

# bonus tip
print(users.duplicated(subset=['age', 'zip_code']).sum())  # 16
print(users.drop_duplicates(subset=['age', 'zip_code']).shape)  # (927, 4)




# Lesson 27: Avoid a SettingWithCopyWarning in pandas

import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)

movies = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\imdb_1000.csv')
print(movies[movies.content_rating.isnull()])  # 只输出True对应的行
print(movies[movies.content_rating == 'NOT RATED'])  # 输出content_rating列内容为'NOT RATED'的行
import numpy as np
# movies[movies.content_rating == 'NOT RATED'].content_rating = np.nan  # 用'NaN'替换'NOT RATED'，错误（SettingWithCopyWarning），因为pandas不知道[]是original还是copy
# print(movies.content_rating.isnull().sum())  # 3
movies.loc[movies.content_rating == 'NOT RATED', 'content_rating'] = np.nan  # 用'NaN'替换'NOT RATED'，正确 loc[行, 列]
print(movies.content_rating.isnull().sum())  # 68

top_movies = movies.loc[movies.star_rating >= 9, :].copy()  # 复制（这样就不会使pandas误解）




# Lesson 28: Change display options in pandas

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# max_rows/columns
drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')
print(pd.get_option('display.max_rows'))  # 60
pd.set_option('display.max_rows', None)
pd.reset_option('display.max_rows')

print(pd.get_option('display.max_columns'))  # 0 （默认是0）

# max_colwidth
train = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\titanic_train.csv')
print(pd.get_option('display.max_colwidth'))  # 50
pd.set_option('display.max_colwidth', 1000)

# precision (decimal point)
print(pd.get_option('precision'))  # 6 (亦可display.precision)
pd.set_option('precision', 3)
print(train.head())
print(train.dtypes)

# bonus tip 1
print(pd.describe_option())  # this is useful while you are not connected to the Internet
print(pd.describe_option('rows'))

# bonus tip 2
pd.reset_option('all')  # reset all options (ignore future warning)




# Lesson 29: Create a pandas DataFrame from another object

import pandas as pd
import numpy as np

print(pd.DataFrame({'id':[100, 101, 102], 'color':['red', 'blue', 'green']}))  # columns of 'id'/'color' are listed in alphabetical order
#     id  color
# 0  100    red
# 1  101   blue
# 2  102  green
print(pd.DataFrame({'color':['red', 'blue', 'green'], 'id':[100, 101, 102]}))
#    color   id
# 0    red  100
# 1   blue  101
# 2  green  102
df = pd.DataFrame({'id':[100, 101, 102], 'color':['red', 'blue', 'green']}, columns=['color', 'id'], index=['a', 'b', 'c'])
print(df)
#    color   id
# a    red  100
# b   blue  101
# c  green  102
print(pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'green']], columns=['id', 'color']))
#     id  color
# 0  100    red
# 1  101   blue
# 2  102  green
arr = np.random.rand(4, 2)
print(pd.DataFrame(arr, columns=['one', 'two']))
#         one       two
# 0  0.240313  0.519416
# 1  0.586056  0.846283
# 2  0.277668  0.239072
# 3  0.769637  0.322811
print(pd.DataFrame({'student': np.arange(100, 104), 'score': np.random.randint(60, 101, 4)}))
#    student  score
# 0      100     90
# 1      101     94
# 2      102     85
# 3      103     97
print(pd.DataFrame({'student': np.arange(100, 104), 'score': np.random.randint(60, 101, 4)}).set_index('student'))
#          score
# student
# 100         91
# 101         95
# 102         63
# 103         97

# bonus tip
print(df)
#    color   id
# a    red  100
# b   blue  101
# c  green  102
s = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')
print(s)
# c     round
# b    square
# Name: shape, dtype: object
print(pd.concat([df, s], axis=1))  # 'shape' becomes the column name
#    color   id   shape
# a    red  100     NaN
# b   blue  101  square
# c  green  102   round




# Lesson 30: Apply a function to a pandas Series or DataFrame

import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)

train = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\titanic_train.csv')
print(train.head())
#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
# 4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S


# map()
train['Sex_num'] = train.Sex.map({'female':0, 'male':1})
print(train.loc[0:4, ['Sex', 'Sex_num']])
#       Sex  Sex_num
# 0    male        1
# 1  female        0
# 2  female        0
# 3  female        0
# 4    male        1


# apply()
# 对元素
train['Name_length'] = train.Name.apply(len)  # 注意len后面无()
print(train.loc[0:4, ['Name', 'Name_length']])
#                                                 Name  Name_length
# 0                            Braund, Mr. Owen Harris           23
# 1  Cumings, Mrs. John Bradley (Florence Briggs Th...           51
# 2                             Heikkinen, Miss. Laina           22
# 3       Futrelle, Mrs. Jacques Heath (Lily May Peel)           44
# 4                           Allen, Mr. William Henry           24

import numpy as np
train['Fare_ceil'] = train.Fare.apply(np.ceil)
print(train.loc[0:4, ['Fare','Fare_ceil']])
#       Fare  Fare_ceil
# 0   7.2500        8.0
# 1  71.2833       72.0
# 2   7.9250        8.0
# 3  53.1000       54.0
# 4   8.0500        9.0

print(train.Name.str.split(',').head())
# 0                           [Braund,  Mr. Owen Harris]
# 1    [Cumings,  Mrs. John Bradley (Florence Briggs ...
# 2                            [Heikkinen,  Miss. Laina]
# 3      [Futrelle,  Mrs. Jacques Heath (Lily May Peel)]
# 4                          [Allen,  Mr. William Henry]
# Name: Name, dtype: object
# def get_element(mylist, position):
#     return mylist[position]
# print(train.Name.str.split(',').apply(get_element, position=0).head())  # 获得第一个名字（apply之前的部分相当于mylist，position=0作为关键字传入）
print(train.Name.str.split(',').apply(lambda x: x[0]).head())  # 与上行等效
# 0       Braund
# 1      Cumings
# 2    Heikkinen
# 3     Futrelle
# 4        Allen
# Name: Name, dtype: object

# 对DataFrame
drinks = pd.read_csv(r'D:\PyCharmCommunityEdition2017.2.4\PyTests\Pandas\csvFiles\drinks.csv')
print(drinks.head())
#        country  beer_servings  spirit_servings  wine_servings  total_litres_of_pure_alcohol continent
# 0  Afghanistan              0                0              0                           0.0      Asia
# 1      Albania             89              132             54                           4.9    Europe
# 2      Algeria             25                0             14                           0.7    Africa
# 3      Andorra            245              138            312                          12.4    Europe
# 4       Angola            217               57             45                           5.9    Africa
print(drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=0))
# beer_servings      376
# spirit_servings    438
# wine_servings      370
# dtype: int64
print(drinks.loc[:, 'beer_servings':'wine_servings'].apply(np.argmax, axis=1).head())  # 最大值所在的列名 future warning
# 0      beer_servings
# 1    spirit_servings
# 2      beer_servings
# 3      wine_servings
# 4      beer_servings
# dtype: object
print(drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float).head())  # apply to every element （original格式未变）
#    beer_servings  spirit_servings  wine_servings
# 0            0.0              0.0            0.0
# 1           89.0            132.0           54.0
# 2           25.0              0.0           14.0
# 3          245.0            138.0          312.0
# 4          217.0             57.0           45.0
drinks.loc[:, 'beer_servings':'wine_servings'] = drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float)  # 改变了original格式
