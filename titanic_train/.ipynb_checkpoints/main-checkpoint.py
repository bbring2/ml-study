import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv('train.csv')

# to use scikit learn, need to replace null as N and avg age for Age column
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)
titanic_df['Cabin'].fillna('N', inplace=True)
titanic_df['Embarked'].fillna('N', inplace=True)

print('Null count : ', titanic_df.isnull().sum().sum())

print('------------------------------------------------')
print('\n 남아있는 문자열 분포값 보기 \n')
print('------------------------------------------------')

print('Sex 값 분포 \n ', titanic_df['Sex'].value_counts())
print('\n Cabin 값 분포 \n ', titanic_df['Cabin'].value_counts())
print('\n Embarked 값 분포 \n ', titanic_df['Embarked'].value_counts())

# TODO : cabin 속성 앞문자만 추출하기
titanic_df['Cabin'] = titanic_df['Cabin'].str[:1]
print(titanic_df['Cabin'].head(3))

# TODO : 성별에 따른 생존자수 비교하기
# 0 - 사망, 1 - 생존
print(titanic_df.groupby(['Sex', 'Survived'])['Survived'].count())

sns.barplot(x='Sex', y='Survived', data=titanic_df).plt.show()
