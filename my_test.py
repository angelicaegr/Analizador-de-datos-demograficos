import pandas as pd

df = pd.read_csv("adult.data.csv")

#print(df['race'].nunique())

#print(df.loc[df['sex'] == "Male", "age"].mean())

#print(df.info())

#print(df['education'])

#print((df['education'] == 'Bachelors').mean())

#print(df['hours-per-week'].min())

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?

#print(((df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')).mean())

#print(df['salary'])

# What country has the highest percentage of people that earn >50K?

#df['high-earner'] = df['salary'] == '>50K'
#highest_earning_country = df.groupby('native-country')['high-earner'].mean().idxmax()

#print(df.groupby('occupation')[df['native-country'] == 'India' & df['salary'] == '>50K'].idmax())
#mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
#mask_2 = mask & (df['salary'] == '>50K')
#mask_3 = ~mask & (df['salary'] == '>50K')
#print((df['salary'] == '>50K').mean())

print(df.info())